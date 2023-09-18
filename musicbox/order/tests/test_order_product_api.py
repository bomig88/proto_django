import json

import pytest

from django.test import TestCase

from order.tests.test_order_product_service import TestOrderProductService


@pytest.mark.django_db
class TestOrderProductApi(TestCase):
    """
    주문 상품 API 테스트 코드
    """
    test_order_product_service = TestOrderProductService()

    def test_api(self):
        self.test_order_product_service.test_crud()
        self.test_api_select_all()
        self.test_api_select()

    def test_api_select_all(self):
        response = self.api_client.get(f'/orders/order-products')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

    def test_api_select(self):
        response = self.api_client.get('/orders/order-products/1')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))
