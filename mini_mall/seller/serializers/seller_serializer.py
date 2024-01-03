from rest_framework import serializers

from seller.models.seller import Seller


class SellerSerializer(serializers.ModelSerializer):
    """
    판매자 Serializer
    """

    def validate_status(self, value):
        """ status 필드 validation
        Args:
            value: 구분값(JOIN: 가입, SANCTIONS: 제재, LEAVE: 탈퇴)
        Returns: value
        """
        # 상태 값이 null인 경우
        if value is not None:
            # 상태 null 값으로 치환
            value = value if value.strip() else None

        # 값이 있을 때만 구분값 체크
        if value and value not in Seller.StatusChoice.values:
            raise Exception('상태를 확인해주세요.')

        return value

    def validate_tag(self, value):
        """ tag 필드 validation
        Args:
            value: 구분값(INDIVIDUAL: 개인 사업체, INCORPORATED: 법인 사업체, TAX_PLAYER: 간이 과세자)
        Returns: value
        """
        # 분류 값이 null인 경우
        if value is not None:
            # 분류 null 값으로 치환
            value = value if value.strip() else None

        # 값이 있을 때만 구분값 체크
        if value and value not in Seller.TagChoice.values:
            raise Exception('분류를 확인해주세요.')

        return value

    def create(self, validated_data):
        # 판매자 등록
        seller = Seller.objects.create(**validated_data)

        return seller

    class Meta:
        model = Seller
        fields = '__all__'


class SellerListSerializer(serializers.ModelSerializer):
    """
    판매자 목록 Serializer
    """

    class Meta:
        model = Seller
        exclude = [
            Seller.business_registration_number.field.name,
            Seller.communication_seller_number.field.name,
            Seller.corporate_registration_number.field.name,
            Seller.sanction_cnt.field.name,
            Seller.customer_center.field.name,
        ]


class SellerDetailSerializer(serializers.ModelSerializer):
    """
    판매자 상세 Serializer
    """

    class Meta:
        model = Seller
        fields = '__all__'
