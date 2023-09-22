from rest_framework import serializers

from core.base.swagger_response_serializer import ResponseSerializer, PagingResponseSerializer
from member.views.serializers.member_serializer import MemberSerializer01


class AuthSerializer01:
    class Field(serializers.Serializer):
        """
        인증 필드 Swagger Serializer
        """
        @staticmethod
        def username(required=False):
            username = serializers.CharField(
                required=required,
                help_text='아이디'
            )
            return username

        @staticmethod
        def password(required=False):
            password = serializers.CharField(
                required=required,
                help_text='비밀번호'
            )
            return password


class AuthSerializer02:
    class LoginPostRequest(serializers.Serializer):
        """
        로그인 요청 Serializer
        """
        username = AuthSerializer01.Field.username(True)
        password = AuthSerializer01.Field.password(True)

        class Meta:
            ref_name = __qualname__

    class LoginPostResponse(ResponseSerializer):
        """
        로그인 응답 Serializer
        """

        class LoginPostResponseData(serializers.Serializer):
            """
            로그인 응답 data Serializer
            """
            refresh_token = serializers.CharField(help_text='Access Token')
            access_token = serializers.CharField(help_text='Access Token')
            refresh_token_lifetime = serializers.IntegerField(help_text='refresh_token lifetime')
            access_token_lifetime = serializers.IntegerField(help_text='access_token lifetime')
            refresh_token_expire_at = serializers.DateTimeField(help_text='refresh_token 만료일시')
            access_token_expire_at = serializers.DateTimeField(help_text='access_token 만료일시')

            class Meta:
                ref_name = __qualname__

        data = LoginPostResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__

    class TokenVerifyPostRequest(serializers.Serializer):
        """
        인증 토큰 유효성 체크 요청 Serializer
        """
        access_token = serializers.CharField(required=True)

        class Meta:
            ref_name = __qualname__

    class TokenRefreshPostRequest(serializers.Serializer):
        """
        인증 토큰 재발급 요청 Serializer
        """
        refresh_token = serializers.CharField(required=True)

        class Meta:
            ref_name = __qualname__

    class TokenRefreshPostResponse(ResponseSerializer):
        """
        인증 토큰 재발급 응답 Serializer
        """

        class TokenRefreshPostResponseData(serializers.Serializer):
            """
            인증 토큰 재발급 응답 data Serializer
            """
            refresh_token = serializers.CharField(help_text='Access Token')
            access_token = serializers.CharField(help_text='Access Token')
            refresh_token_lifetime = serializers.IntegerField(help_text='refresh_token lifetime')
            access_token_lifetime = serializers.IntegerField(help_text='access_token lifetime')
            refresh_token_expire_at = serializers.DateTimeField(help_text='refresh_token 만료일시')
            access_token_expire_at = serializers.DateTimeField(help_text='access_token 만료일시')

            class Meta:
                ref_name = __qualname__

        data = TokenRefreshPostResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__

    class TestGetParam(serializers.Serializer):
        """
        목록 조회 파라미터 Serializer
        """

        username = MemberSerializer01.Field.username()

        class Meta:
            ref_name = __qualname__

    class TestGetResponse(PagingResponseSerializer):
        """
        목록 조회 응답 Serializer
        """

        class TestGetResponseData(serializers.Serializer):
            """
            관리자 목록 조회 응답 data Serializer
            """
            members = serializers.ListField(
                child=MemberSerializer01.Default(),
                required=False,
                help_text="코드"
            )

            class Meta:
                ref_name = __qualname__

        data = TestGetResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__

    class TestDetailGetParam(serializers.Serializer):
        """
        목록 조회 파라미터 Serializer
        """

        class Meta:
            ref_name = __qualname__

    class TestDetailGetResponse(ResponseSerializer):
        """
        상세 조회 응답 Serializer
        """

        class TestDetailGetResponseData(serializers.Serializer):
            """
            상세 조회 응답 data Serializer
            """
            member = MemberSerializer01.Default()

            class Meta:
                ref_name = __qualname__

        data = TestDetailGetResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__
