from django.contrib import admin

from order.models.order import Order
from order.models.order_product import OrderProduct

admin.site.register(Order)
admin.site.register(OrderProduct)
