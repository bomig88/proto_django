from django.conf import settings
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator

from core.auth.base_user import AbstractBaseUser
from core.auth.base_user_manager import BaseUserManager
from core.auth.permissions_mixin import PermissionsMixin
from core.utils.datetime_util import DatetimeUtil
from core.fields.encrypted_char_field import Sha256EncryptedCharField


class Member(AbstractBaseUser, PermissionsMixin):
    """
    회원 모델
    """
    class GenderChoice(models.TextChoices):
        M = 'M', '남성'
        F = 'F', '여성'
        N = 'N', '미설정'

    class StatusChoice(models.TextChoices):
        JOIN = 'join', '가입'
        LEAVE = 'leave', '탈퇴'

    class TagChoice(models.TextChoices):
        BASIC_USER = 'basic_user', '일반 사용자'
        MANAGER = 'manager', '관리자'
        SUPER_MANAGER = 'super_manager', '상위 관리자'

    # 생년월일 날짜 포맷
    BIRTHDAY_FORMAT = '%Y%m%d'
    # 인증 관련 USERNAME 필드
    USERNAME_FIELD = "username"
    # 이메일 필드 지정
    EMAIL_FIELD = "email"
    # 인증 관련 사용자 사용 여부 필드
    ISACTIVE_FIELD = "status"

    objects = BaseUserManager()

    seq = models.BigAutoField(
        primary_key=True,
        help_text='일련번호(PK)'
    )
    password = Sha256EncryptedCharField(
        null=True,
        max_length=300,
        help_text='비밀번호'
    )
    username = models.CharField(
        max_length=50,
        validators=[UnicodeUsernameValidator()],
        unique=True,
        help_text='이름'
    )
    email = models.EmailField(
        unique=True,
        help_text='이메일 주소'
    )
    gender = models.CharField(
        choices=GenderChoice.choices,
        max_length=1,
        help_text='성별(M:남, F:여, N:미설정)',
        default=GenderChoice.N.value
    )
    birthday = models.CharField(
        null=True,
        max_length=8,
        help_text='생년월일'
    )
    status = models.CharField(
        choices=StatusChoice.choices,
        max_length=30,
        help_text='상태',
        default=StatusChoice.JOIN.value
    )
    tag = models.CharField(
        choices=TagChoice.choices,
        max_length=30,
        help_text='분류',
        default=TagChoice.BASIC_USER.value
    )
    is_active = models.BooleanField(
        default=True,
        help_text='활성화 여부'
    )
    last_login_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text='최종 로그인 일시'
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        help_text='생성일시'
    )
    update_at = models.DateTimeField(
        auto_now=True,
        help_text='수정일시'
    )
    leave_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text='탈퇴일'
    )

    @property
    def is_superuser(self):
        return self.tag == Member.TagChoice.SUPER_MANAGER.value

    @property
    def is_staff(self):
        return self.tag in [Member.TagChoice.SUPER_MANAGER.value, Member.TagChoice.MANAGER.value]

    @property
    def is_user(self):
        return self.tag in [Member.TagChoice.BASIC_USER.value]

    def use_validation(self):
        is_use_valid = True

        if self.status != self.StatusChoice.JOIN:
            # 탈퇴, 휴면, 잠금 상태에 해당
            is_use_valid = False

        return is_use_valid

    @staticmethod
    def birthday_validation(params: dict):
        """
        생년월일 유효성 체크합니다.
        Args:
            params: 회원 dict
        Returns:
        Raises: CustomValidationException
        """
        if params.get('birthday', None):
            if not DatetimeUtil.validate_date_str(params['birthday'], Member.BIRTHDAY_FORMAT):
                raise Exception(f'유효하지 않은 생년월일입니다.')

    @classmethod
    def get_token_infos(cls, refresh) -> dict:
        """회원 토큰 정보를 가져옵니다
        Args:
            refresh: refresh 토큰
        Returns:회원 토큰 정보(dict)
        """
        token_info = dict()
        token_info['refresh_token'] = str(refresh)
        token_info['access_token'] = str(refresh.access_token)
        token_info['access_token_lifetime'] = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
        token_info['refresh_token_lifetime'] = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
        # access_token, refresh_token 만료시간 추가
        token_info['access_token_expire_at'] = DatetimeUtil.datetime_delta(
            refresh.access_token.current_time, seconds=refresh.access_token.lifetime.total_seconds()
        )
        token_info['refresh_token_expire_at'] = DatetimeUtil.datetime_delta(
            refresh.current_time, seconds=refresh.lifetime.total_seconds()
        )
        return token_info

    class Meta:
        db_table = 't_mb_member'
        unique_together = ('email', 'tag')
        ordering = ['-seq']
