import datetime
import json
from unittest import TestCase

import pytest

from _musicbox.containers import Services
from member.models.order import Order
from member.tests.test_member_service import TestMemberService
from member.tests.test_order_product_service import TestOrderProductService


@pytest.mark.django_db
class TestOrderCycle(TestCase):
    order_service = Services.order_service()
    test_member_service = TestMemberService()
    test_order_product_service = TestOrderProductService()

    def test_add(self, params=None):
        if not params:
            member_instance = self.test_member_service.test_create()
            paid_at = datetime.datetime.now()

            params = dict()
            params['member_seq'] = member_instance['seq']
            params['paid_at'] = paid_at
            params['status'] = Order.StatusChoice.PAID.value

            params['order_products'] = self.test_order_product_service.get_test_order_product_dict(paid_at)

        print('params')
        print(params)

        serializer = self.order_service.add(params)

        print('serializer')
        print(json.dumps(serializer.data, ensure_ascii=False))

        return serializer.data
