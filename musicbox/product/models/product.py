from django.db import models
from django_currentuser.db.models import CurrentUserField

from seller.models.seller import Seller


class Product(models.Model):
    """
    상품 모델
    """
    class StatusChoice(models.TextChoices):
        ENABLE = 'enable', '판매중'
        DISABLE = 'disable', "판매 중지"
        SANCTIONS = 'sanctions', '제재'

    objects = None

    seq = models.BigAutoField(
        primary_key=True,
        help_text='일련번호(PK)'
    )
    seller_seq = models.ForeignKey(
        Seller,
        null=False,
        on_delete=models.PROTECT,
        db_column='seller_seq',
        db_constraint=True,
        help_text='판매자 일련번호(FK)'
    )
    name = models.CharField(
        null=False,
        max_length=120,
        help_text='이름'
    )
    representation_image = models.CharField(
        null=True,
        max_length=512,
        help_text='대표이미지'
    )
    org_price = models.IntegerField(
        help_text='소비자가'
    )
    sale_price = models.IntegerField(
        help_text='판매가'
    )
    discount_rate = models.SmallIntegerField(
        help_text='할인율'
    )
    tax_flag = models.SmallIntegerField(
        default=1,
        help_text='과세여부'
    )
    counsel_telephone = models.CharField(
        null=True,
        max_length=64,
        help_text='소비자상담번호'
    )
    status = models.CharField(
        choices=StatusChoice.choices,
        max_length=30,
        help_text='상태',
        default=StatusChoice.DISABLE.value
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
        return self.status == Product.StatusChoice.ENABLE.value

    class Meta:
        db_table = 't_pd_product'
        ordering = ['-seq']