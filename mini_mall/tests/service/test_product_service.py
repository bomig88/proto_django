import pytest
from django.test import TestCase

from config.containers import Services
from seller.models.seller import Seller


@pytest.mark.django_db
class TestProductService(TestCase):
    product_service = Services.product_service()
    seller_service = Services.seller_service()

    def test_crud(self):
        # register
        # 판매자 먼저 등록
        individual_seller_params = dict()
        individual_seller_params['name'] = "개인사업체"
        individual_seller_params['representative'] = "개인사업체 대표"
        individual_seller_params['corporate_registration_number'] = None
        individual_seller_params['business_registration_number'] = "111-11-111"
        individual_seller_params['communication_seller_number'] = "1211-11-1"
        individual_seller_params['customer_center'] = "11-111"
        individual_seller_params['tag'] = Seller.TagChoice.INDIVIDUAL.value

        register_individual_seller = self.seller_service.create(individual_seller_params)
        assert register_individual_seller.data.get('tag') == Seller.TagChoice.INDIVIDUAL.value

        product_params = dict()
        product_params['seller_seq'] = register_individual_seller.data.get('seq')
        product_params['name'] = "상품1010"
        product_params['representation_image'] = "이미지가 들어옵니다"
        product_params['org_price'] = 12000
        product_params['sale_price'] = 6000
        product_params['discount_rate'] = 50
        product_params['tax_flag'] = 1
        product_params['counsel_telephone'] = '1212-11'

        register_product = self.product_service.create(product_params)
        assert register_product.data.get('org_price') == 12000

        product_seq = register_product.data.get('seq')
        path_param = {'seq': product_seq}

        # select
        select_serializer = self.product_service.select(path_param=path_param)
        assert select_serializer.data.get('seq') == product_seq

        # select_all
        serializer = self.product_service.select_all(params=None)
        assert len(serializer.data) > 0

        # select_all_model
        models = self.product_service.select_all_model(params=None)
        assert models

        # modify
        name = '상품수정2111'
        modify_params = {'name': name}
        modify_seller_serializer = self.product_service.modify(
            path_param=path_param,
            params=modify_params,
            partial=True)
        assert modify_seller_serializer.data.get('name') == name
