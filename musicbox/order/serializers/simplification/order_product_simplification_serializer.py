from rest_framework import serializers

from order.models.order import Order
from order.models.order_product import OrderProduct


class OrderProductSimplificationSerializer(serializers.ModelSerializer):
    """
    주문 상품 간소화 Serializer
    """
    class Meta:
        model = OrderProduct
        fields = [
            OrderProduct.seq.field.name,
            OrderProduct.order_seq.field.name,
            OrderProduct.music_seq.field.name,
            OrderProduct.status.field.name,
            OrderProduct.price.field.name,
            OrderProduct.paid_at.field.name,
            OrderProduct.refund_at.field.name,
            OrderProduct.create_at.field.name,
            OrderProduct.update_at.field.name,
        ]
