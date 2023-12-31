from django.urls import path

from product.views.product_views import ProductView, ProductDetailView

urlpatterns = [
    path('', ProductView.as_view()),
    path('/<int:seq>', ProductDetailView.as_view())
]