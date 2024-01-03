import pytest
from django.test import TestCase

from seller.models.seller import Seller


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client")
class TestProductApi(TestCase):
    """
    상품 API 테스트
    """
    def test_api(self):
        #### register test start
        # 판매자 먼저 등록
        individual_seller_params = dict()
        individual_seller_params['name'] = "개인사업체"
        individual_seller_params['representative'] = "개인사업체 대표"
        individual_seller_params['corporate_registration_number'] = None
        individual_seller_params['business_registration_number'] = "111-11-111"
        individual_seller_params['communication_seller_number'] = "1211-11-1"
        individual_seller_params['customer_center'] = "11-111"
        individual_seller_params['tag'] = Seller.TagChoice.INDIVIDUAL.value

        # register
        individual_seller_response = self.api_client.post('/sellers', individual_seller_params, format='json')
        print(f'individual_seller register.status_code = {individual_seller_response.status_code}')
        print('individual_seller register response.data', individual_seller_response.data, end='\n')
        assert individual_seller_response.status_code == 200
        assert individual_seller_response.data['success'] == True

        product_params = dict()
        product_params['seller_seq'] = individual_seller_response.data['data']['seller']['seq']
        product_params['name'] = "상품1010"
        product_params['representation_image'] = "이미지가 들어옵니다"
        product_params['org_price'] = 12000
        product_params['sale_price'] = 6000
        product_params['discount_rate'] = 50
        product_params['tax_flag'] = 1
        product_params['counsel_telephone'] = '1212-11'

        # register
        product_response = self.api_client.post('/products', product_params, format='json')
        print(f'product register.status_code = {product_response.status_code}')
        print('product register response.data', product_response.data, end='\n')
        assert product_response.status_code == 200
        assert product_response.data['success'] == True

        #### register test complete

        product_seq = product_response.data['data']['product']['seq']

        # select
        response = self.api_client.get(f'/products/{product_seq}')
        print(f'select.status_code = {response.status_code}')
        print('select response.data', response.data, end='\n')
        assert response.status_code == 200
        assert response.data['success'] == True
        assert response.data['data']['product']['seq'] == product_seq

        # select_all
        response = self.api_client.get('/products?page=1')
        print(f'select_all.status_code = {response.status_code}')
        print('select_all response.data', response.data, end='\n')
        assert response.status_code == 200
        assert response.data['success'] == True
        assert len(response.data['data']['products']) > 0

        # modify
        name = '상품수정2111'
        modify_params = {'name': name}

        response = self.api_client.patch(f'/products/{product_seq}', modify_params, format="json")
        print(f'select_all.status_code = {response.status_code}')
        print('select_all response.data', response.data, end='\n')
        assert response.status_code == 200
        assert response.data['success'] == True
        assert response.data['data']['product']['name'] == name
