from core.base.base_service import BaseService
from product.filters.product_filter import ProductFilter
from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer, ProductListSerializer, ProductDetailSerializer
from seller.models.seller import Seller


class ProductService(BaseService):
    queryset_list = Product.objects\
        .select_related(Product.seller_seq.field.name)\
        .all()
    queryset_detail = Product.objects\
        .select_related(Product.seller_seq.field.name)\
        .all()
    serializer = ProductSerializer
    serializer_list = ProductListSerializer
    serializer_detail = ProductDetailSerializer
    filter_set_class = ProductFilter

    def create(self, params: dict):
        # 판매자 존재 유무 및 탈퇴 또는 제재 판매자인지 확인
        seller_seq = params.get('seller_seq', None)
        if seller_seq:
            from config.containers import Services
            seller = Services.seller_service().select_model({'seq': params.get('seller_seq')})
            if seller:
                if seller.status == Seller.StatusChoice.SANCTIONS.value:
                    raise Exception('제재된 판매자입니다. 상품을 등록할 수 없습니다.')
                elif seller.status == Seller.StatusChoice.LEAVE.value:
                    raise Exception('탈퇴한 판매자입니다. 상품을 등록할 수 없습니다.')

            else:
                raise Exception('판매자를 찾을 수 없습니다. 판매자 일련번호를 확인해 주세요.')
        else:
            raise Exception('판매자 일련번호 정보를 찾을 수 없습니다. 판매자 일련번호를 확인해 주세요.')

        params['status'] = Product.StatusChoice.ENABLE.value

        return super().create(params)
