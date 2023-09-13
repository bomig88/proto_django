from django.urls import path


from order.views.order_views import OrderView, OrderDetailView
from order.views.order_product_views import OrderProductView, OrderProductDetailView

urlpatterns = [
    path('', OrderView.as_view()),
    path('<int:seq>', OrderDetailView.as_view()),

    path('order-products', OrderProductView.as_view()),
    path('order-products/<int:seq>', OrderProductDetailView.as_view()),
]
