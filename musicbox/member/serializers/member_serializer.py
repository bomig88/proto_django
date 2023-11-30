from rest_framework import serializers

from member.models.member import Member


class MemberSerializer(serializers.ModelSerializer):
    """
    회원 Serializer
    """
    password = serializers.CharField(write_only=True)
    simplicity_key = serializers.CharField(write_only=True, required=False)

    def validate_birthday(self, value):
        """ 생년월일 필드 validation
        Args:
            value: 생년월일
        Returns: value
        """
        # 생년월일 값이 null인 경우
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
        # 성별 값이 null인 경우
        if value is not None:
            # 성별 null 값으로 치환
            value = value if value.strip() else None

        # 값이 있을 때만 구분값 체크
        if value and value not in Member.GenderChoice.values:
            raise Exception('성별을 확인해주세요.')

        return value

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

    def validate_tag(self, value):
        """ tag 필드 validation
        Args:
            value: 구분값(BASIC_USER: 일반 유저, SIMPLICITY_USER: 간편 가입 유저, MANAGER: 관리자, SUPER_MANAGER: 상위 관리자)
        Returns: value
        """
        # 분류 값이 null인 경우
        if value is not None:
            # 분류 null 값으로 치환
            value = value if value.strip() else None

        # 값이 있을 때만 구분값 체크
        if value and value not in Member.TagChoice.values:
            raise Exception('분류를 확인해주세요.')

        return value

    def create(self, validated_data):
        # 회원 등록
        member = Member.objects.create(**validated_data)

        return member

    class Meta:
        model = Member
        fields = '__all__'


class MemberListSerializer(serializers.ModelSerializer):
    """
    회원 목록 Serializer
    """

    class Meta:
        model = Member
        exclude = [
            Member.password.field.name,
            Member.groups.field.name,
            Member.user_permissions.field.name,
        ]


class MemberDetailSerializer(serializers.ModelSerializer):
    """
    회원 상세 Serializer
    """

    class Meta:
        model = Member
        exclude = [
            Member.password.field.name,
            Member.groups.field.name,
            Member.user_permissions.field.name,
        ]
