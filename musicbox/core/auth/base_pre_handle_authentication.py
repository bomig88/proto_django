from rest_framework.authentication import BaseAuthentication
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import HTTP_HEADER_ENCODING, authentication

from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken, TokenError
from rest_framework_simplejwt.settings import api_settings
from core.utils.logging_util import LoggingUtil


AUTH_HEADER_TYPES = api_settings.AUTH_HEADER_TYPES

if not isinstance(api_settings.AUTH_HEADER_TYPES, (list, tuple)):
    AUTH_HEADER_TYPES = (AUTH_HEADER_TYPES,)

AUTH_HEADER_TYPE_BYTES = set(
    h.encode(HTTP_HEADER_ENCODING)
    for h in AUTH_HEADER_TYPES
)

User = get_user_model()


class BasePreHandleAuthentication(BaseAuthentication):
    """
        SimpleJWT Token 인증
    """
    logger = LoggingUtil()
    www_authenticate_realm = 'api'

    def authenticate(self, request):
        """ 토큰 유효성 체크
        Args:
            request: 요청
        Returns: 사용자 정보, 유효성 확인된 토큰
        """
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token

    def authenticate_header(self, request):
        """ 헤더 설정값 확인
        Args:
            request: 요청
        Returns: 설정값
        """
        return '{0} realm="{1}"'.format(
            AUTH_HEADER_TYPES[0],
            self.www_authenticate_realm,
        )

    def get_header(self, request):
        """헤더에서 토큰 추출
        Args:
            request: 요청
        Returns: 헤더 정보
        """
        header = request.META.get(api_settings.AUTH_HEADER_NAME)

        if isinstance(header, str):
            # Work around django test client oddness
            header = header.encode(HTTP_HEADER_ENCODING)

        return header

    def get_raw_token(self, header):
        """헤더에서 Authorization 정보 추출
        Args:
            header: 헤더
        Returns: Authorization 정보값
        """
        parts = header.split()

        if len(parts) == 0:
            # Empty AUTHORIZATION header sent
            return None

        if parts[0] not in AUTH_HEADER_TYPE_BYTES:
            # Assume the header does not contain a JSON web token
            return None

        if len(parts) != 2:
            raise AuthenticationFailed(
                _('Authorization header에 공백으로 구분된 두 개의 값이 포함되어야 합니다.'),
                code='bad_authorization_header',
            )

        return parts[1]

    def get_validated_token(self, raw_token):
        """ 토큰의 유효성 검증
        Args:
            raw_token: 토큰
        Returns: 검증된 토큰
        """
        messages = []
        for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
            try:
                return AuthToken(raw_token)
            except TokenError as e:
                messages.append({'token_class': AuthToken.__name__,
                                 'token_type': AuthToken.token_type,
                                 'message': e.args[0]})

        raise InvalidToken({
            'detail': _('토큰이 유효하지 않습니다.'),
            'messages': messages,
        })

    def get_user(self, validated_token):
        """검증된 토큰 정보를 기반으로 사용자를 반환
        Args:
            validated_token: 검증된 토큰
        Returns: 사용자 정보
        """
        try:
            user_id = validated_token[api_settings.USER_ID_CLAIM]
        except KeyError:
            raise InvalidToken(_('토큰에 사용자 정보가 없습니다.'))

        try:
            user = User.objects.get(**{api_settings.USER_ID_FIELD: user_id})
        except User.DoesNotExist:
            raise AuthenticationFailed(_('사용자를 찾지 못했습니다.'), code='user_not_found')

        if not user.is_active:
            raise AuthenticationFailed(_('사용자가 비활성화 상태입니다.'), code='user_inactive')

        return user
