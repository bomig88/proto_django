from django.db import models
from django.db.models.expressions import Col

from django.conf import settings
from Crypto.Hash import SHA256


class CryptoSha256:
    def __init__(self, key: str):
        self.key = key

    def encrypt(self, plain_text: str) -> str:
        """
            SHA256 단방향 암호화
            Python_시큐어코딩_가이드.pdf 73 페이지 참고
        """

        # print(f'plain_text : {plain_text}')

        if plain_text is None:
            return plain_text

        hash_obj = SHA256.new()
        hash_obj.update(bytes(plain_text + self.key, 'utf-8'))

        return hash_obj.hexdigest()


class Sha256EncryptedCharField(models.CharField):
    """
     단방향 암호화 필드
    """

    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        self.org_value = None
        super(Sha256EncryptedCharField, self).__init__(max_length=max_length, *args, **kwargs)

    def from_db_value(self, value: str, expression: Col, connection) -> str:
        """데이터베이스에서 반환된 필드 값 가져오기
        """
        self.org_value = value
        return value

    def get_prep_value(self, value: str) -> str:
        """
            Python 객체를 데이터베이스 값으로 변환
        """
        if value and CryptoSha256(settings.SECRET_KEY).encrypt(self.org_value) != CryptoSha256(settings.SECRET_KEY).encrypt(value):
            return CryptoSha256(settings.SECRET_KEY).encrypt(value)
        else:
            return value

    def value_from_object(self, obj):
        """ 전달 받은 모델에서 해당 필드하는 값을 가져옵니다.
        Args:
            obj: 모델
        Returns: 전달 받은 모델에서 해당 필드하는 값
        """
        if getattr(obj, self.attname):
            setattr(
                obj,
                self.attname,
                CryptoSha256(settings.SECRET_KEY).encrypt(getattr(obj, self.attname))
            )

        return getattr(obj, self.attname)
