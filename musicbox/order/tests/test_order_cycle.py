import json
from unittest import TestCase

import pytest

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

    def test_service(self):
        self.test_add()

    def test_add(self, params=None):
        if not params:
            params = dict()
            params['order_products'] = self.test_order_product_service.get_test_order_product_dict()

        print('params')
        print(params)

        serializer = self.order_service.add(params)

        print('serializer')
        print(json.dumps(serializer.data, ensure_ascii=False))

        return serializer.data
