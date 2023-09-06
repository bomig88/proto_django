from rest_framework import serializers

from content.serializers.music_serializer import MusicSerializer
from member.models.order_product import OrderProduct
from member.serializers.simplification.order_simplification_serializer import OrderSimplificationSerializer


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'


class OrderProductListSerializer(serializers.ModelSerializer):
    music = MusicSerializer(
        many=False,
        read_only=True,
        source=OrderProduct.music_seq.field.name
    )

    class Meta:
        model = OrderProduct
        fields = '__all__'


class OrderProductDetailSerializer(serializers.ModelSerializer):
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