from django.db import models

from content.models.music import Music
from member.models.order import Order


class OrderProduct(models.Model):
    object = None

    class StatusChoice(models.TextChoices):
        PAID = 'paid', '구매 완료'
        REFUND = 'refund', '환불'

    seq = models.BigAutoField(
        primary_key=True,
        help_text='일련번호(PK)'
    )

    order_seq = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        db_column='order_seq',
        db_constraint=False,
        help_text='주문 일련번호'
    )

    music_seq = models.ForeignKey(
        Music,
        on_delete=models.CASCADE,
        db_column='music_seq',
        db_constraint=False,
        help_text='곡 일련번호'
    )

    status = models.CharField(
        choices=StatusChoice.choices,
        max_length=30,
        help_text='상태'
    )

    price = models.IntegerField(
        default=0,
        help_text='판매가'
    )

    paid_at = models.DateTimeField(
        null=True,
        help_text='구매 일시'
    )

    refund_at = models.DateTimeField(
        null=True,
        help_text='환불 일시'
    )

    create_at = models.DateTimeField(
        auto_now_add=True,
        help_text='생성일시'
    )

    update_at = models.DateTimeField(
        auto_now=True,
        help_text='수정일시'
    )

    class Meta:
        db_table = 't_usr_order_product'
        ordering = ['-seq']
