from django.contrib import admin
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm, DateField

from order.models.order import Order
from order.models.order_product import OrderProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('seq', 'username', 'status', 'paid_at', 'create_at')
    list_select_related = ['member_seq']  # To avoid extra queries

    def username(self, order):
        return order.member_seq.username  # Foreign key relationship


class OrderProductCreationForm(ModelForm):
    refund_at = DateField(label='refund_at', required=False, widget=AdminDateWidget)

    class Meta:
        model = OrderProduct
        fields = ('order_seq', 'music_seq', 'status', 'price', 'paid_at', 'refund_at')


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('seq', 'order_seq', 'music_seq', 'music_name', 'status', 'price', 'paid_at', 'refund_at', 'create_at')
    list_select_related = ['music_seq']  # To avoid extra queries
    add_form = OrderProductCreationForm

    def music_name(self, order_product):
        return order_product.music_seq.name  # Foreign key relationship

