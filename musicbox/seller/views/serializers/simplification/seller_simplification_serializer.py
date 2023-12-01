from rest_framework import serializers

from seller.models.seller import Seller


class SellerSimplificationSerializer01:
    """
    Swagger 판매자 간소화 Serializer
    """
    class Default(serializers.ModelSerializer):

        class Meta:
            model = Seller
            fields = '__all__'
            ref_name = __qualname__
