from content.models.music import Music
from core.base.base_service import BaseService
from order.filters.order_product_filter import OrderProductFilter
from order.models.order_product import OrderProduct
from order.serializers.order_product_serializer import OrderProductSerializer, OrderProductDetailSerializer, \
    OrderProductListSerializer


class OrderProductService(BaseService):
    """
    주문 상품 서비스
    """
    queryset_list = (OrderProduct.objects
                     .all())
    queryset_detail = (OrderProduct.objects
                       .select_related(OrderProduct.music_seq.field.name)
                       .select_related(OrderProduct.order_seq.field.name).all())
    serializer = OrderProductSerializer
    serializer_list = OrderProductListSerializer
    serializer_detail = OrderProductDetailSerializer
    filter_set_class = OrderProductFilter

    def bulk_create(self, order, order_products):
        """
        주문 상품 무더기 생성
        Args:
            order: 주문 상품이 속한 주문 모델
            order_products: 주문 상품 목록
        Returns:
            생성된 주문 상품 목록
        """
        for op in order_products:
            op['order_seq'] = order
            music_instance = Music.objects.get(seq=op['music_seq'])
            op['music_seq'] = music_instance
            op['price'] = music_instance.price
            op['paid_at'] = order.paid_at
            op['status'] = OrderProduct.StatusChoice.PAID.value

        bulk_order_products = list(map(lambda x: OrderProduct.convert_dict_to_model(x), order_products))

        OrderProduct.objects.bulk_create(bulk_order_products)

        return bulk_order_products
