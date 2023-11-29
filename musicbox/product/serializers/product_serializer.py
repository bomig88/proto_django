from rest_framework import serializers

from member.models.member import Member
from product.models.product import Product
from seller.serializers.simplification.seller_simplification_serializer import SellerSimplificationSerializer


class ProductSerializer(serializers.ModelSerializer):
    """
    상품 Serializer
    """
    seller = SellerSimplificationSerializer(
        many=False,
        required=True,
        source=Product.seller_seq.field.name
    )

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
        if value and value not in Member.StatusChoice.values:
            raise Exception('상태를 확인해주세요.')

        return value

    def create(self, validated_data):
        if validated_data.get(Member.tag.field.name,
                              Member.TagChoice.BASIC_USER.value) == Member.TagChoice.SIMPLICITY_USER.value \
                and not validated_data.get(Member.simplicity_key.field.name, None):
            raise Exception('간편 인증 값을 확인해주세요.')

        # 회원 등록
        member = Member.objects.create(**validated_data)

        return member

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
