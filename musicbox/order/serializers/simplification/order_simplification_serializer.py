from rest_framework import serializers

from order.models.order import Order


class OrderSimplificationSerializer(serializers.ModelSerializer):
    """
    주문 간소화 Serializer
    """
    class Meta:
        model = Order
        fields = [
            Order.seq.field.name,
            Order.member_seq.field.name,
            Order.status.field.name,
            Order.paid_at.field.name,
            Order.create_at.field.name,
            Order.update_at.field.name,
        ]
