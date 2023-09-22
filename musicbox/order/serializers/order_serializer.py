from rest_framework import serializers

from member.serializers.simplification.member_simplification_serializer import MemberSimplificationSerializer
from order.models.order import Order
from order.models.order_product import OrderProduct
from order.serializers.simplification.order_product_simplification_serializer import \
    OrderProductSimplificationSerializer


class OrderSerializer(serializers.ModelSerializer):
    """
    주문 Serializer
    """
    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    """
    주문 목록 Serializer
    """
    member = MemberSimplificationSerializer(
        many=False,
        read_only=True,
        source=Order.member_seq.field.name
    )

    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    """
    주문 상세 Serializer
    """
    member = MemberSimplificationSerializer(
        many=False,
        read_only=True,
        source=Order.member_seq.field.name
    )

    order_products = OrderProductSimplificationSerializer(
        many=True,
        required=False,
        source=f'{OrderProduct.__name__.lower()}_set'
    )

    class Meta:
        model = Order
        fields = '__all__'
