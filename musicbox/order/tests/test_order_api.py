import json

import pytest

from django.test import TestCase

from order.tests.test_order_service import TestOrderService


@pytest.mark.django_db
class TestOrderApi(TestCase):
    test_order_service = TestOrderService()

    def test_api(self):
        self.test_order_service.test_crud()
        self.test_api_select_all()
        self.test_api_select()

    def test_api_select_all(self):
        response = self.api_client.get('/orders/')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

    def test_api_select(self):
        response = self.api_client.get('/orders/1')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))
