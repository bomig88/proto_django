from rest_framework import serializers

from product.models.product import Product


class ProductSimplificationSerializer01:
    """
    Swagger 상품 간소화 Serializer
    """
    class Default(serializers.ModelSerializer):

        class Meta:
            model = Product
            fields = '__all__'
            ref_name = __qualname__
