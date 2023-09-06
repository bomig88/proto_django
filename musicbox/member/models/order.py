from django.db import models

from member.models.member import Member


class Order(models.Model):
    objects = None

    class StatusChoice(models.TextChoices):
        PAID = 'paid', '구매 완료'
        SOME_REFUND = 'some_refund', '일부 환불'
        REFUND = 'refund', '전체 환불'

    seq = models.BigAutoField(
        primary_key=True,
        help_text='일련번호(PK)'
    )

    member_seq = models.OneToOneField(
        Member,
        on_delete=models.CASCADE,
        db_column='member_seq',
        db_constraint=False,
        related_name='member',
        help_text='회원 일련번호'
    )

    paid_at = models.DateTimeField(
        null=True,
        help_text='구매 일시'
    )

    status = models.CharField(
        choices=StatusChoice.choices,
        max_length=30,
        help_text='상태'
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
        db_table = 't_usr_order'
        ordering = ['-seq']
