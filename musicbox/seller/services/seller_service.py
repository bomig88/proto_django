from core.base.base_service import BaseService
from seller.filters.seller_filter import SellerFilter
from seller.models.seller import Seller
from seller.serializers.seller_serializer import SellerSerializer, SellerListSerializer, SellerDetailSerializer


class SellerService(BaseService):
    """
    판매자 서비스
    """
    queryset_list = Seller.objects.all()
    queryset_detail = Seller.objects.all()
    serializer = SellerSerializer
    serializer_list = SellerListSerializer
    serializer_detail = SellerDetailSerializer
    filter_set_class = SellerFilter

    def create(self, params: dict):

        params['status'] = Seller.StatusChoice.JOIN.value

        return super().create(params)