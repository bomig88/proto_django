from rest_framework import serializers

from product.models.product import Product
from seller.serializers.simplification.seller_simplification_serializer import SellerSimplificationSerializer


class ProductSerializer(serializers.ModelSerializer):
    """
    상품 Serializer
    """
    def validate_status(self, value):
        """ status 필드 validation
        Args:
            value: 구분값(JOIN: 가입, LEAVE: 탈퇴)
        Returns: value
        """
        # 상태 값이 null인 경우
        if value is not None:
            # 상태 null 값으로 치환
            value = value if value.strip() else None

        # 값이 있을 때만 구분값 체크
        if value and value not in Product.StatusChoice.values:
            raise Exception('상태를 확인해주세요.')

        return value

    def create(self, validated_data):
        # 회원 등록
        product = Product.objects.create(**validated_data)

        return product

    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    """
    상품 목록 Serializer
    """
    seller = SellerSimplificationSerializer(
        many=False,
        required=True,
        source=Product.seller_seq.field.name
    )

    class Meta:
        model = Product
        exclude = [
            Product.counsel_telephone.field.name,
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    """
    상품 상세 Serializer
    """
    seller = SellerSimplificationSerializer(
        many=False,
        required=True,
        source=Product.seller_seq.field.name
    )

    class Meta:
        model = Product
        fields = '__all__'
