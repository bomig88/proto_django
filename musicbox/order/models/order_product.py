from django.db import models

from content.models.music import Music
from order.models.order import Order


class OrderProduct(models.Model):
    """
    주문 상품 모델
    """
    objects = None

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

    @staticmethod
    def convert_dict_to_model(dic: dict):
        order_product = OrderProduct()

        if 'seq' in dic:
            order_product.seq = dic['seq']

        order_product.order_seq = dic.get('order_seq')
        order_product.music_seq = dic.get('music_seq')
        order_product.status = dic.get('status')
        order_product.price = dic.get('price')
        order_product.paid_at = dic.get('paid_at')
        order_product.refund_at = dic.get('refund_at')

        if 'create_at' in dic:
            order_product.create_at = dic.get('create_at')
        if 'update_at' in dic:
            order_product.update_at = dic.get('update_at')

        return order_product

    class Meta:
        db_table = 't_usr_order_product'
        ordering = ['-seq']
