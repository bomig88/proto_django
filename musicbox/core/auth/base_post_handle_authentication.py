import traceback
import datetime
import redis
import json

from django.contrib.auth import get_user_model, logout, login
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.backends import BaseBackend
from django.db import models


from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from core.fields.encrypted_char_field import CryptoSha256
from core.utils.datetime_util import DatetimeUtil
from django.conf import settings
from core.utils.logging_util import LoggingUtil
from member.serializers.simplification.member_simplification_serializer import MemberSimplificationLoginSerializer
from core.base.redis_config import redis_config


class BasePostHandleAuthentication(BaseBackend):
    """
    공통 인증
    """
    UserModel = get_user_model()
    logger = LoggingUtil()
    rd = redis_config()

    NM = '사용자'

    def get_user(self, user_id):
        try:
            self.logger.info(f'catch get_user={user_id}')
            return self.UserModel.objects.get(pk=user_id)
        except (Exception,):
            return None

    def authenticate(self, request, username: str = None, password: str = None, **kwargs: dict) -> models:
        """ 전달 받은 사용자에 대한 인증 확인을 합니다
        Args:
            request: 요청
            username: 사용자 명
            password: 비밀번호
            **kwargs: username 대체 값(dict)
        Returns: 사용자 모델
        """
        if username is None:
            username = kwargs.get(self.UserModel.USERNAME_FIELD)

        if username is None or password is None:
            return None

        try:
            # self.logger.info(f'AUTH_USER_MODEL={settings.AUTH_USER_MODEL}')
            # self.logger.info(type(self.UserModel))
            user = getattr(self.UserModel, '_default_manager').get_by_natural_key(username)
        except (Exception,):
            self.logger.error(f'not found username={username}')
            return None

        if self.check_password(user, password):
            return user
        else:
            return None

    @staticmethod
    def check_password(user: models, raw_password: str) -> bool:
        """ 비밀번호에 대한 유효성 체크합니다
        Args:
            user: 인증 기준 모델
            raw_password: 비밀번호
        Returns: 유효성 체크 결과
        """
        return getattr(user, 'password', None) == CryptoSha256(settings.SECRET_KEY).encrypt(raw_password)

    def token(self, request, **kwargs: dict):
        """ token(access_token, refresh_token) 값을 가져옵니다
        Args:
            request: 요청
            **kwargs: username 대체 값(dict)
        Returns: refresh token, access token, refresh token lifetime, access token lifetime 정보
        Raises:
            Exception
        """
        path_params = request.data

        if 'username' not in path_params or not path_params['username']:
            raise Exception('아이디를 확인해 주세요.')
        if 'password' not in path_params or not path_params['password']:
            raise Exception('비밀번호를 확인해 주세요.')

        # 사용자 인증 확인
        user = self.authenticate(
            request=request,
            username=path_params['username'],
            password=path_params['password'],
            **kwargs
        )

        if not user:
            raise Exception(f'일치하는 {self.NM}가 없습니다.')

        self.user_can_authenticate(user)

        login(request, user)

        # 최종 로그인 일시 업데이트
        # django 기본 요건인 last_login 정보와 필드 이름이 달라져서(last_login_at)
        # 자동 업데이트가 이루어지지 않아 수동으로 업데이트 해야 합니다
        # getattr(user, 'last_login_at', None)으로 항목 검증 시 last_login_at의 값이 None인 경우가 있어서 조건 변경
        if getattr(user, 'last_login_at', 'not_found') != 'not_found':
            user.last_login_at = datetime.datetime.now()
            user.save(update_fields=['last_login_at'])

        refresh = RefreshToken.for_user(user)

        self.claim_for_token(request, user, refresh)

        response = dict()
        response['refresh_token'] = str(refresh)
        response['access_token'] = str(refresh.access_token)
        response['access_token_lifetime'] = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
        response['refresh_token_lifetime'] = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
        # access_token, refresh_token 만료시간 추가
        response['access_token_expire_at'] = DatetimeUtil.datetime_delta(
            refresh.access_token.current_time, seconds=refresh.access_token.lifetime.total_seconds()
        )
        response['refresh_token_expire_at'] = DatetimeUtil.datetime_delta(
            refresh.current_time, seconds=refresh.lifetime.total_seconds()
        )
        serialize_user = MemberSimplificationLoginSerializer(user, many=False).data
        response['member'] = serialize_user

        # redis cache save
        self.rd.set(user.seq, json.dumps(serialize_user))

        return response

    def claim_for_token(self, request, user: models, refresh):
        """토큰 정보에 추가 데이터 적재
        Args:
            request: 요청
            refresh: 토큰
            user: 사용자 모델
        Returns: None
        """
        pass

    def user_can_authenticate(self, user: models):
        """사용자 활성화 상태 체크
        Args:
            user: 인증 기준 모델
        Returns: None
        Raises:
            Exception
        """
        if not getattr(user, self.UserModel.ISACTIVE_FIELD, None):
            raise Exception('사용할 수 없는 사용자 입니다.')

    @staticmethod
    def token_verify(view: TokenVerifyView, path_params: dict):
        """ 토큰 유효성을 체크합니다
        Args:
            view: simplejwt TokenVerifyView
            path_params: access token path_params(dict)
        Returns: 유효성 체크 결과
        Raises:
            Exception, InvalidToken
        """
        if 'access_token' not in path_params or not path_params['access_token']:
            raise Exception('access_token을 확인해 주세요.')

        serializer = view.get_serializer(data={'token': path_params['access_token']})
        is_token_verify = False

        try:
            if serializer.is_valid(raise_exception=True):
                is_token_verify = True
        except TokenError as e:
            is_token_verify = False
            # 토큰 유효성 관련 return 변경
            # raise InvalidToken('토큰이 유효하지 않습니다.')

        return is_token_verify

    @staticmethod
    def token_refresh(view: TokenRefreshView, path_params: dict):
        """ 토큰을 재발급합니다
        Args:
            view: simplejwt TokenRefreshView
            path_params: refresh token path_params(dict)
        Returns: refresh token, access token, refresh token lifetime, access token lifetime 정보
        Raises:
            Exception, TokenError
        """
        if 'refresh_token' not in path_params or not path_params['refresh_token']:
            raise Exception('refresh_token을 확인해 주세요')

        print(path_params['refresh_token'])

        serializer = view.get_serializer(data={'refresh': path_params['refresh_token']})

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken('토큰이 유효하지 않습니다.')

        refresh = serializer.token_class(serializer.validated_data['refresh'])

        response = dict()
        response['refresh_token'] = str(refresh)
        response['access_token'] = str(refresh.access_token)
        response['access_token_lifetime'] = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
        response['refresh_token_lifetime'] = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
        # access_token, refresh_token 만료시간 추가
        response['access_token_expire_at'] = DatetimeUtil.datetime_delta(
            refresh.access_token.current_time, seconds=refresh.access_token.lifetime.total_seconds()
        )
        response['refresh_token_expire_at'] = DatetimeUtil.datetime_delta(
            refresh.current_time, seconds=refresh.lifetime.total_seconds()
        )

        return response

    def logout(self, request):
        """ 로그아웃합니다.
        Args: None
        Returns: None
        Raises:
            Exception
        """
        try:
            if not request.user or isinstance(request.user, AnonymousUser):
                raise Exception('로그인 사용자 정보가 없습니다.')

            user_seq = request.user.seq
            logout(request)
            # redis cache delete
            self.rd.delete(user_seq)

            return True
        except (Exception) as error:
            self.logger.error(traceback.format_exc())
            raise Exception('로그아웃에 실패했습니다.')

    def get_user_permissions(self, user_obj, obj=None):
        """ 사용자 메뉴 권한 체크
        Args:
            user_obj: 사용자 모델
            obj: 파악 중
        Returns: 권한 목록
        """
        return set()

    def get_group_permissions(self, user_obj, obj=None):
        """ 사용자 그룹 권한 체크
        Args:
            user_obj: 사용자 모델
            obj: 파악 중
        Returns: 권한 목록
        """
        return set()

    def get_all_permissions(self, user_obj, obj=None):
        """ 사용자 메뉴 권한과 사용자 그룹 권한 조회
        Args:
            user_obj: 사용자 모델
            obj: 파악 중
        Returns: 권한 목록
        """
        return {
            *self.get_user_permissions(user_obj, obj=obj),
            *self.get_group_permissions(user_obj, obj=obj),
        }

    def has_perm(self, user_obj, perm, obj=None):
        """ 사용자 권한 체크
        Args:
            user_obj: 사용자 모델
            perm: 체크할 권한 정보 (path)
            obj: 파악 중
        Returns: 접근 가능 여부
        """
        return perm.startswith(tuple(self.get_all_permissions(user_obj, obj=obj)))
