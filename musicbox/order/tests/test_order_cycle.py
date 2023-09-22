import json
import random

import pytest
from unittest import TestCase

from _musicbox.containers import Services
from member.tests.test_member_service import TestMemberService
from order.tests.test_order_product_service import TestOrderProductService


@pytest.mark.django_db
class TestOrderCycle(TestCase):
    """
    주문 플로우 테스트 코드
    """
    order_service = Services.order_service()
    test_member_service = TestMemberService()
    test_order_product_service = TestOrderProductService()

    def test_add_some_refund_service(self):
        """ 주문 등록 후 일부 환불 케이스 테스트 """
        # 주문 등록
        order = self.test_add({
            'member_seq': self.member_seq,
            'order_products': self.test_order_product_service.get_test_order_product_dict()
        })

        # 환불할 주문 상품 랜덤 추출
        order_products = order['order_products']
        order_product_seqs = ','.join(list(map(lambda x: str(x['seq']), random.sample(order_products, 2))))

        # 환불
        self.test_refund({'seq': order['seq'], 'order_product_seqs': order_product_seqs})

    def test_add_all_refund_service(self):
        """ 주문 등록 후 전체 환불 케이스 테스트 """
        # 주문 등록
        order = self.test_add({
            'member_seq': self.member_seq,
            'order_products': self.test_order_product_service.get_test_order_product_dict()
        })

        # 환불할 주문 상품 전체 추출
        order_products = order['order_products']
        order_product_seqs = ','.join(list(map(lambda x: str(x['seq']), order_products)))

        # 환불
        self.test_refund({'seq': order['seq'], 'order_product_seqs': order_product_seqs})

    def test_add(self, params):
        print('params')
        print(params)

        serializer = self.order_service.add(params)

        print('serializer')
        print(json.dumps(serializer.data, ensure_ascii=False))

        return serializer.data

    def test_refund(self, params):
        print('params')
        print(params)

        serializer = self.order_service.refund(params)

        print('serializer')
        print(json.dumps(serializer.data, ensure_ascii=False))

        return serializer.data
