from django.contrib import admin

from member.models.member import Member
from member.models.order import Order
from member.models.order_product import OrderProduct

admin.site.register(Member)
admin.site.register(Order)
admin.site.register(OrderProduct)
