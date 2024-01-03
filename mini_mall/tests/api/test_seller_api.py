import pytest
from django.test import TestCase

from seller.models.seller import Seller


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client")
class TestSellerApi(TestCase):
    """
    판매자 API 테스트 코드
    """
    def test_api(self):
        #### register test start
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

        incorporated_seller_params = dict()
        incorporated_seller_params['name'] = "법인사업체"
        incorporated_seller_params['representative'] = "법인사업체 대표"
        incorporated_seller_params['corporate_registration_number'] = "2232-22-222"
        incorporated_seller_params['business_registration_number'] = "22-222-22"
        incorporated_seller_params['communication_seller_number'] = "2122-22-2"
        incorporated_seller_params['customer_center'] = "22-222"
        incorporated_seller_params['tag'] = Seller.TagChoice.INCORPORATED.value

        # register
        incorporated_seller_response = self.api_client.post('/sellers', incorporated_seller_params, format='json')
        print(f'incorporated_seller register.status_code = {incorporated_seller_response.status_code}')
        print('incorporated_seller register response.data', incorporated_seller_response.data, end='\n')
        assert incorporated_seller_response.status_code == 200
        assert incorporated_seller_response.data['success'] == True

        tax_player_seller_params = dict()
        tax_player_seller_params['name'] = "간이과세자"
        tax_player_seller_params['representative'] = "간이과세자 대표"
        tax_player_seller_params['corporate_registration_number'] = "3232-33-333"
        tax_player_seller_params['business_registration_number'] = "33-333-33"
        tax_player_seller_params['communication_seller_number'] = "3213-33-3"
        tax_player_seller_params['customer_center'] = "33-333"
        tax_player_seller_params['tag'] = Seller.TagChoice.TAX_PLAYER.value

        # register
        tax_player_seller_response = self.api_client.post('/sellers', tax_player_seller_params, format='json')
        print(f'tax_player_seller register.status_code = {tax_player_seller_response.status_code}')
        print('tax_player_seller register response.data', tax_player_seller_response.data, end='\n')
        assert tax_player_seller_response.status_code == 200
        assert tax_player_seller_response.data['success'] == True

        #### register test complete

        individual_seller_seq = individual_seller_response.data['data']['seller']['seq']

        # select
        response = self.api_client.get(f'/sellers/{individual_seller_seq}')
        print(f'select.status_code = {response.status_code}')
        print('select response.data', response.data, end='\n')
        assert response.status_code == 200
        assert response.data['success'] == True
        assert response.data['data']['seller']['seq'] == individual_seller_seq

        # select_all
        response = self.api_client.get('/sellers?page=1')
        print(f'select_all.status_code = {response.status_code}')
        print('select_all response.data', response.data, end='\n')
        assert response.status_code == 200
        assert response.data['success'] == True
        assert len(response.data['data']['sellers']) > 0

        # modify
        name = '개인과세자였던무언가'
        modify_params = {'name': name}

        response = self.api_client.patch(f'/sellers/{individual_seller_seq}', modify_params, format="json")
        print(f'select_all.status_code = {response.status_code}')
        print('select_all response.data', response.data, end='\n')
        assert response.status_code == 200
        assert response.data['success'] == True
        assert response.data['data']['seller']['name'] == name
