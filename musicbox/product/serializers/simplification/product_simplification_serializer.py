from rest_framework import serializers

from product.models.product import Product


class ProductSimplificationSerializer(serializers.ModelSerializer):
    """
    상품 간소화 Serializer
    """
    class Meta:
        model = Product
        fields = [
            Product.seq.field.name,
            Product.name.field.name,
            Product.seller_seq.field.name,
            Product.status.field.name,
            Product.create_at.field.name,
            Product.update_at.field.name,
        ]
