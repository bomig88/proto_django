from rest_framework import serializers

from seller.models.seller import Seller


class SellerSimplificationSerializer(serializers.ModelSerializer):
    """
    판매자 간소화 Serializer
    """
    class Meta:
        model = Seller
        fields = [
            Seller.seq.field.name,
            Seller.name.field.name,
            Seller.representative.field.name,
            Seller.status.field.name,
            Seller.tag.field.name,
            Seller.create_at.field.name,
            Seller.update_at.field.name,
        ]
