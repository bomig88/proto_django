from content.filters.album_filter import AlbumFilter
from content.models.album import Album
from content.models.music import Music
from content.serializers.album_serializer import AlbumSerializer
from core.base.base_service import BaseService
from member.filters.order_filter import OrderFilter
from member.models.member import Member
from member.models.order import Order
from member.models.order_product import OrderProduct
from member.serializers.order_serializer import OrderSerializer, OrderListSerializer, OrderDetailSerializer


class OrderService(BaseService):
    queryset_list = (Order.objects.select_related('member_seq')
                     .prefetch_related(f'{OrderProduct.__name__.lower()}_set').all())
    queryset_detail = (Order.objects.select_related('member_seq')
                       .prefetch_related(f'{OrderProduct.__name__.lower()}_set').all())
    serializer = OrderSerializer
    serializer_list = OrderListSerializer
    serializer_detail = OrderDetailSerializer
    filter_set_class = OrderFilter

    def add(self, params: dict):
        order_products = params.pop('order_products')

        serializer = super().create(params)

        order_dict = serializer.data
        order_dict['member_seq'] = Member.objects.get(seq=order_dict['member_seq'])
        order = Order(**order_dict)

        from _musicbox.containers import Services
        order_product_service = Services.order_product_service()
        order_product_service.bulk_create(order, order_products)

        return serializer
