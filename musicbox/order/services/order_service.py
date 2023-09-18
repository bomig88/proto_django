import datetime

from core.base.base_service import BaseService
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

    def add(self, params: dict):
        """
        주문 모델 및 연관 모델 등록
        Args:
            params: 주문 모델 및 연관 모델 구성 정보
            - order
                - member_seq: 회원 일련번호
                - order_products: 주문 상품 구성 정보 목록
        Returns:
            생성된 주문 Serializer
        """
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
