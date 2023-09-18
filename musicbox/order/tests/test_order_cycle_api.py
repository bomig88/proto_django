import json
from unittest import TestCase

import pytest

from _musicbox.containers import Services
from member.tests.test_member_service import TestMemberService
from order.tests.test_order_product_service import TestOrderProductService


@pytest.mark.django_db
class TestOrderCycleApi(TestCase):
    """
    주문 플로우 API 테스트 코드
    """
    order_service = Services.order_service()
    test_member_service = TestMemberService()
    test_order_product_service = TestOrderProductService()

    def test_api(self):
        self.test_api_add_success()
        self.test_api_add_fail()

    def test_api_add_success(self):
        orders = {
            'member_seq': 1,
            'order_products': self.test_order_product_service.get_test_order_product_dict()
        }
        response = self.api_client.post('/orders', orders, format='json')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

    def test_api_add_fail(self):
        orders = {
            'order_products': self.test_order_product_service.get_test_order_product_dict()
        }
        response = self.api_client.post('/orders', orders, format='json')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))