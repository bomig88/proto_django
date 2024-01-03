import pytest
from django.test import TestCase

from config.containers import Services
from seller.models.seller import Seller


@pytest.mark.django_db
class TestSellerService(TestCase):
    seller_service = Services.seller_service()

    def test_crud(self):
        # register
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

        incorporated_seller_params = dict()
        incorporated_seller_params['name'] = "법인사업체"
        incorporated_seller_params['representative'] = "법인사업체 대표"
        incorporated_seller_params['corporate_registration_number'] = "2232-22-222"
        incorporated_seller_params['business_registration_number'] = "22-222-22"
        incorporated_seller_params['communication_seller_number'] = "2122-22-2"
        incorporated_seller_params['customer_center'] = "22-222"
        incorporated_seller_params['tag'] = Seller.TagChoice.INCORPORATED.value

        register_incorporated_seller = self.seller_service.create(incorporated_seller_params)
        assert register_incorporated_seller.data.get('tag') == Seller.TagChoice.INCORPORATED.value

        tax_player_seller_params = dict()
        tax_player_seller_params['name'] = "간이과세자"
        tax_player_seller_params['representative'] = "간이과세자 대표"
        tax_player_seller_params['corporate_registration_number'] = "3232-33-333"
        tax_player_seller_params['business_registration_number'] = "33-333-33"
        tax_player_seller_params['communication_seller_number'] = "3213-33-3"
        tax_player_seller_params['customer_center'] = "33-333"
        tax_player_seller_params['tag'] = Seller.TagChoice.TAX_PLAYER.value

        register_tax_player_seller = self.seller_service.create(tax_player_seller_params)
        assert register_tax_player_seller.data.get('tag') == Seller.TagChoice.TAX_PLAYER.value

        seller_seq = register_individual_seller.data.get('seq')
        path_param = {'seq': seller_seq}

        # select
        select_serializer = self.seller_service.select(path_param=path_param)
        assert select_serializer.data.get('seq') == seller_seq

        # select_all
        serializer = self.seller_service.select_all(params=None)
        assert len(serializer.data) > 0

        # select_all_model
        models = self.seller_service.select_all_model(params=None)
        assert models

        # modify
        name = '개인과세자였던무언가'
        modify_params = {'name': name}
        modify_seller_serializer = self.seller_service.modify(
            path_param=path_param,
            params=modify_params,
            partial=True)
        assert modify_seller_serializer.data.get('name') == name
