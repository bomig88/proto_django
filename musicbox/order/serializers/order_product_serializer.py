from rest_framework import serializers

from content.serializers.music_serializer import MusicSerializer
from order.models.order_product import OrderProduct
from order.serializers.simplification.order_simplification_serializer import OrderSimplificationSerializer


class OrderProductSerializer(serializers.ModelSerializer):
    """
    주문 상품 Serializer
    """
    class Meta:
        model = OrderProduct
        fields = '__all__'


class OrderProductListSerializer(serializers.ModelSerializer):
    """
    주문 상품 목록 Serializer
    """
    class Meta:
        model = OrderProduct
        fields = '__all__'


class OrderProductDetailSerializer(serializers.ModelSerializer):
    """
    주문 상품 상세 Serializer
    """
    music = MusicSerializer(
        many=False,
        read_only=True,
        source=OrderProduct.music_seq.field.name
    )

    order = OrderSimplificationSerializer(
        many=False,
        read_only=True,
        source=OrderProduct.order_seq.field.name
    )

    class Meta:
        model = OrderProduct
        fields = '__all__'
