from rest_framework import serializers

from member.models.order import Order


class OrderSimplificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
