from django.db import models
from django.db.backends.postgresql.base import DatabaseWrapper
from django.db.models.expressions import Col
from django_currentuser.middleware import get_current_authenticated_user


class CurrentUserField(models.CharField):
    """
    관리자 필드
    """

    def __init__(self, max_length, *args, **kwargs):
        self.on_update = kwargs.pop("on_update", False)
        self.max_length = max_length
        self.value = None

        super(CurrentUserField, self).__init__(max_length=max_length, *args, **kwargs)

    def from_db_value(self, value: str, expression: Col, connection: DatabaseWrapper) -> str:
        """데이터베이스에서 반환된 필드 값 가져오기
        """
        self.value = value
        return value

    @classmethod
    def get_username(cls):
        """ 현재 사용자 아이디를 가져옵니다.
        Returns: 사용자 아이디
        """
        return get_current_authenticated_user()

    def pre_save(self, model_instance: models.Model, add: bool) -> str:
        """ 저장 직전 모델 내 해당 필드 값을 반환합니다.
        Args:
            model_instance: 모델
            add: 등록 실행 여부
        Returns: 저장 직전 필드 값
        """
        username = self.get_username()

        if add:
            # 모델 내 등록하는 경우
            if username:
                setattr(model_instance, self.attname, username)
            return getattr(model_instance, self.attname)
        else:
            # 모델 내 수정하는 경우
            if self.on_update:
                if username:
                    setattr(model_instance, self.attname, username.username)
                return getattr(model_instance, self.attname)

            else:
                # create_by 필드는 최초 등록한 값 기준으로 설정
                setattr(model_instance, self.attname, self.value)
                return getattr(model_instance, self.attname)

    def value_from_object(self, obj: models.Model) -> str:
        """ 전달 받은 모델에서 해당 필드하는 값을 가져옵니다.
        Args:
            obj: 모델
        Returns: 전달 받은 모델에서 해당 필드하는 값
        """
        username = self.get_username()

        if not getattr(obj, self.attname):
            setattr(obj, self.attname, username)
        return getattr(obj, self.attname)
