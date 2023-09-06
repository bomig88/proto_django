from content.models.music import Music
from core.base.base_service import BaseService
from member.filters.order_product_filter import OrderProductFilter
from member.models.order_product import OrderProduct
from member.serializers.order_product_serializer import OrderProductSerializer, OrderProductDetailSerializer, \
    OrderProductListSerializer


class OrderProductService(BaseService):
    queryset_list = (OrderProduct.objects.select_related('music_seq').all())
    queryset_detail = (OrderProduct.objects.select_related('music_seq')
                       .select_related('order_seq').all())
    serializer = OrderProductSerializer
    serializer_list = OrderProductListSerializer
    serializer_detail = OrderProductDetailSerializer
    filter_set_class = OrderProductFilter

    def bulk_create(self, order, order_products):
        for op in order_products:
            op['order_seq'] = order
            op['music_seq'] = Music.objects.get(seq=op['music_seq'])

        p = list(map(lambda x: OrderProduct.convert_dict_to_model(x), order_products))

        print(p)

        OrderProduct.objects.bulk_create(p)
