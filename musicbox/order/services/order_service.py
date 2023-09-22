import datetime

from django.db import transaction

from core.base.base_service import BaseService
from core.utils.logging_util import LoggingUtil
from order.filters.order_filter import OrderFilter
from member.models.member import Member
from order.models.order import Order
from order.models.order_product import OrderProduct
from order.serializers.order_serializer import OrderSerializer, OrderListSerializer, OrderDetailSerializer


class OrderService(BaseService):
    """
    주문 서비스
    """
    queryset_list = (Order.objects
                     .select_related(Order.member_seq.field.name)
                     .all())
    queryset_detail = (Order.objects
                       .select_related(Order.member_seq.field.name)
                       .prefetch_related(f'{OrderProduct.__name__.lower()}_set').all())
    serializer = OrderSerializer
    serializer_list = OrderListSerializer
    serializer_detail = OrderDetailSerializer
    filter_set_class = OrderFilter

    logger = LoggingUtil()

    @transaction.atomic
    def add(self, params: dict):
        """
        주문 모델 및 연관 모델 등록
        Args:
            params: 주문 모델 및 연관 모델 구성 정보
            - order
                - order_products: 주문 상품 구성 정보 목록
        Returns:
            생성된 주문 Serializer
        """
        self.logger.info(f'order create params = {params}')
        order_products = params.pop('order_products')

        paid_at = datetime.datetime.now()

        params['paid_at'] = paid_at
        params['status'] = Order.StatusChoice.PAID.value

        serializer = super().create(params)

        order_dict = serializer.data
        order_dict['member_seq'] = Member.objects.get(seq=order_dict['member_seq'])

        order = Order(**order_dict)

        from _musicbox.containers import Services
        order_product_service = Services.order_product_service()
        order_product_service.bulk_create(order, order_products)

        return super().select(path_param={'seq': serializer.data.get('seq')})

    @transaction.atomic
    def refund(self, params: dict):
        """
        주문 및 주문 상품 환불 처리
        Args:
            params: 환불 대상 주문 및 주문 상품 일련번호
                - seq : 주문 일련번호
                - order_product_seqs: 주문 상품 일련번호 (구분 ',')
                    - ex: 8,2,12
        Returns:
            변경된 주문 및 주문 상품 정보
        """
        path_param = dict()
        path_param['seq'] = params['seq']

        # 주문 정보 조회해서 존재하는 정보인지 확인
        order_serializer = super().select(path_param)

        # 주문 상품의 정보를 환불로 업데이트
        from _musicbox.containers import Services
        order_product_service = Services.order_product_service()

        op_path_params = dict()
        op_path_params['order_seq'] = params['seq']
        op_path_params['seqs'] = params['order_product_seqs']

        refund_order_products = order_product_service.select_all_model(op_path_params)
        for refund_order_product in refund_order_products:
            op_modify_params = dict()
            op_modify_params['refund_at'] = datetime.datetime.now()
            op_modify_params['status'] = OrderProduct.StatusChoice.REFUND.value

            order_product_service.modify({'seq': refund_order_product.seq}, op_modify_params, partial=True)

        # 주문의 주문상품 전체 조회하여 환불 상태 대조 후 주문의 상태를 일부 환불 또는 환불로 변경 처리
        order_products = order_product_service.select_all_model({'order_seq': params['seq']})
        order_product_cnt = len(order_products)
        refund_cnt = len(list(filter(lambda x: x.status == OrderProduct.StatusChoice.REFUND.value, order_products)))

        modify_params = dict()
        modify_params['status'] = Order.StatusChoice.REFUND.value if order_product_cnt == refund_cnt else Order.StatusChoice.SOME_REFUND.value

        serializer = super().modify(path_param, modify_params, partial=True)

        return serializer
