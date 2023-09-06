from rest_framework import serializers

from member.models.order import Order
from member.models.order_product import OrderProduct
from member.serializers.member_serializer import MemberSerializer
from member.serializers.order_product_serializer import OrderProductListSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    member = MemberSerializer(
        many=False,
        read_only=True,
        source=Order.member_seq.field.name
    )

    order_products = OrderProductListSerializer(
        many=True,
        required=False,
        source=f'{OrderProduct.__name__.lower()}_set'
    )

    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):


    class Meta:
        model = Order
        fields = '__all__'