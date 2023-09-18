from rest_framework import serializers

from member.models.member import Member


class MemberSerializer(serializers.ModelSerializer):
    """
    회원 Serializer
    """
    password = serializers.CharField(allow_blank=True)

    def validate_birthday(self, value):
        """ 생년월일 필드 validation
        Args:
            value: 생년월일
        Returns: value
        """
        # 생년월일 값이 nill인 경우
        if value is not None:
            # 생년월일 null 값으로 치환
            value = value if value.strip() else None

        Member.birthday_validation({'birthday': value})

        return value

    def validate_gender(self, value):
        """ gender 필드 validation
        Args:
            value: 구분값(M: 남성, F: 여성, N: 미설정)
        Returns: value
        """
        # 성별 값이 nill인 경우
        if value is not None:
            # 성별 null 값으로 치환
            value = value if value.strip() else None

        # 값이 있을 때만 구분값 체크
        if value and value not in Member.GenderChoice.values:
            raise Exception('성별을 확인해주세요.')

        return value

    class Meta:
        model = Member
        fields = '__all__'


class MemberListSerializer(serializers.ModelSerializer):
    """
    회원 목록 Serializer
    """
    class Meta:
        model = Member
        fields = '__all__'


class MemberDetailSerializer(serializers.ModelSerializer):
    """
    회원 상세 Serializer
    """
    class Meta:
        model = Member
        fields = '__all__'
