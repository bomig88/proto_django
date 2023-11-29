from django.db import models
from django_currentuser.db.models import CurrentUserField


class Seller(models.Model):
    """
    판매자 모델
    """
    class StatusChoice(models.TextChoices):
        JOIN = 'join', '가입'
        SANCTIONS = 'sanctions', '제재'
        LEAVE = 'leave', '탈퇴'

    class TagChoice(models.TextChoices):
        INDIVIDUAL = 'individual', "개인 사업체"
        INCORPORATED = 'incorporated', "법인 사업체"
        TAX_PLAYER = 'tax_player', '간이 과세자'

    objects = None

    seq = models.BigAutoField(
        primary_key=True,
        help_text='일련번호(PK)'
    )
    name = models.CharField(
        null=False,
        max_length=50,
        help_text='이름'
    )
    representative = models.CharField(
        max_length=50,
        help_text='대표자명'
    )
    corporate_registration_number = models.CharField(
        unique=True,
        null=True,
        max_length=50,
        help_text='법인등록번호'
    )
    business_registration_number = models.CharField(
        unique=True,
        max_length=50,
        help_text='사업자등록번호'
    )
    communication_seller_number = models.CharField(
        unique=True,
        max_length=50,
        help_text='통신판매업신고번호'
    )
    customer_center = models.CharField(
        max_length=50,
        help_text='고객센터 연락처'
    )
    sanction_cnt = models.IntegerField(
        default=0,
        help_text='재제횟수'
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
        default=TagChoice.INDIVIDUAL.value
    )
    create_by = CurrentUserField(
        max_length=64,
        help_text='생성자'
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        help_text='생성일시'
    )
    update_by = CurrentUserField(
        max_length=64,
        on_update=True,
        help_text='수정자'
    )
    update_at = models.DateTimeField(
        auto_now=True,
        help_text='수정일시'
    )

    @property
    def is_active(self):
        return self.status == Seller.StatusChoice.JOIN.value

    class Meta:
        db_table = 't_mb_seller'
        ordering = ['-seq']