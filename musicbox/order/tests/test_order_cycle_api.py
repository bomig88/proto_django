import json
import random
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

    def test_add_api(self):
        self.test_api_add_success()
        self.test_api_add_fail()

    def test_refund_api(self):
        # 주문 부분 환불 테스트
        order = self.test_api_add_success()
        some_order_product_seqs = ','.join(list(map(lambda x: str(x['seq']), random.sample(order['order_products'], 2))))
        self.test_api_some_refund_success(order['seq'], some_order_product_seqs)

        # 주문 전체 환불 테스트
        order = self.test_api_add_success()
        order_product_seqs = ','.join(list(map(lambda x: str(x['seq']), order['order_products'])))
        self.test_api_all_refund_success(order['seq'], order_product_seqs)

    def test_api_all_refund_success(self, order_seq, order_product_seqs):
        response = self.api_client.post(f'/orders/{order_seq}/refund', {'order_product_seqs': order_product_seqs}, format='json')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

    def test_api_some_refund_success(self, order_seq, order_product_seqs):
        response = self.api_client.post(f'/orders/{order_seq}/refund', {'order_product_seqs': order_product_seqs}, format='json')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

    def test_api_add_success(self):
        orders = {
            'order_products': self.test_order_product_service.get_test_order_product_dict()
        }
        response = self.api_client.post('/orders', orders, format='json')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

        return response.data['data']['order']

    def test_api_add_fail(self):
        orders = {
            'order_products': self.test_order_product_service.get_test_order_product_dict()
        }
        response = self.api_client.post('/orders', orders, format='json')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))
