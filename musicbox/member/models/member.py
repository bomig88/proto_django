from django.conf import settings
from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import check_password, is_password_usable, make_password
from django.utils.crypto import salted_hmac

from utils.datetime_util import DatetimeUtil
from utils.encrypted_char_field import Sha256EncryptedCharField


class MemberManager(AbstractBaseUser, PermissionsMixin):
    use_in_migrations = True


    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('Email을 입력해주세요.')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff=True일 필요가 있습니다.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser=True일 필요가 있습니다.')
        return self._create_user(username, email, password, **extra_fields)


class Member(AbstractBaseUser, PermissionsMixin):
    class GenderChoice(models.TextChoices):
        M = 'M', '남성'
        F = 'F', '여성'
        N = 'N', '미설정'

    class StatusChoice(models.TextChoices):
        JOIN = 'join', '가입'
        LEAVE = 'leave', '탈퇴'

    # 생년월일 날짜 포맷
    BIRTHDAY_FORMAT = '%Y%m%d'

    # 인증 관련 사용자 사용 여부 필드
    ISACTIVE_FIELD = "status"

    objects = MemberManager()

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
        help_text='이름'
    )
    email = models.EmailField(
        unique=True,
        help_text='이메일 주소'
    )
    gender = models.CharField(
        null=True,
        max_length=1,
        help_text='성별(M:남, F:여, N:미설정)'
    )
    birthday = models.CharField(
        null=True,
        max_length=8,
        help_text='생년월일'
    )
    status = models.CharField(
        choices=StatusChoice.choices,
        max_length=30,
        help_text='상태'
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
        null=True,
        help_text='탈퇴일'
    )

    def use_validation(self):
        is_use_valid = True

        if self.status != self.StatusChoice.JOIN:
            # 탈퇴, 휴면, 잠금 상태에 해당
            is_use_valid = False

        return is_use_valid

    def birthday_validation(self, params: dict):
        """
        생년월일 유효성 체크합니다.
        Args:
            params: 회원 dict
        Returns:
        Raises: CustomValidationException
        """
        if params.get('birthday', None):
            if not DatetimeUtil.validate_date_str(params['birthday'], self.BIRTHDAY_FORMAT):
                raise Exception(f'유효하지 않은 생년월일입니다.')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)

    def set_unusable_password(self):
        # Set a value that will never be a valid hash
        self.password = make_password(None)

    def has_usable_password(self):
        return is_password_usable(self.password)

    def _legacy_get_session_auth_hash(self):
        key_salt = 'django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash'
        return salted_hmac(key_salt, self.password, algorithm='sha1').hexdigest()

    def get_session_auth_hash(self):
        key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
        return salted_hmac(
            key_salt,
            self.password,
            # RemovedInDjango40Warning: when the deprecation ends, replace
            # with:
            # algorithm='sha256',
            algorithm=settings.DEFAULT_HASHING_ALGORITHM,
        ).hexdigest()

    @classmethod
    def get_token_infos(cls, refresh) -> dict:
        """회원 토큰 정보를 가져옵니다
        Args:
            refresh: refresh 토큰
        Returns:회원 토큰 정보(dict)
        """
        token_infos = dict()
        token_infos['refresh_token'] = str(refresh)
        token_infos['access_token'] = str(refresh.access_token)
        token_infos['access_token_lifetime'] = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
        token_infos['refresh_token_lifetime'] = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
        # access_token, refresh_token 만료시간 추가
        token_infos['access_token_expire_at'] = DatetimeUtil.datetime_delta(
            refresh.access_token.current_time, seconds=refresh.access_token.lifetime.total_seconds()
        )
        token_infos['refresh_token_expire_at'] = DatetimeUtil.datetime_delta(
            refresh.current_time, seconds=refresh.lifetime.total_seconds()
        )
        return token_infos

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None

    @classmethod
    def get_email_field_name(cls):
        try:
            return cls.EMAIL_FIELD
        except AttributeError:
            return 'email'

    class Meta:
        abstract = True
        db_table = 't_mb_member'
        unique_together = ('username', 'email')
        ordering = ['-seq']
