from django.urls import path

from seller.views.seller_views import SellerView, SellerDetailView

urlpatterns = [
    path('', SellerView.as_view()),
    path('/<int:seq>', SellerDetailView.as_view())
]