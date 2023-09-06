import datetime
import json

import pytest
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.test import TestCase

from _musicbox.containers import Services
from content.tests.test_music_service import TestMusicService
from member.models.order_product import OrderProduct
from member.tests.test_order_service import TestOrderService


@pytest.mark.django_db
class TestOrderProductService(TestCase):
    order_product_service = Services.order_product_service()
    test_order_service = TestOrderService()
    test_music_service = TestMusicService()

    def test_crud(self):
        print('--create--')
        instance = self.test_create()

        path_param = {'seq': instance['seq']}

        print('--select--')
        self.test_select(params=path_param)

        print('--select_model--')
        self.test_select_model(params=path_param)

        print('--modify--')
        self.test_modify(path_param=path_param, modify_params={'price': 9000})

        print('--select_all--')
        self.test_select_all(params={})

        print('--select_all_model--')
        self.test_select_all_model(params={})

    def get_test_order_product_dict(self, paid_at):
        m1 = self.test_music_service.test_create()
        op1 = dict()
        op1['music_seq'] = m1['seq']
        op1['status'] = OrderProduct.StatusChoice.PAID.value
        op1['price'] = m1['price']
        op1['paid_at'] = paid_at

        m2 = self.test_music_service.test_create()
        op2 = dict()
        op2['music_seq'] = m2['seq']
        op2['status'] = OrderProduct.StatusChoice.PAID.value
        op2['price'] = m2['price']
        op2['paid_at'] = paid_at

        order_products = [op1, op2]

        return order_products

    def test_create(self, params=None):
        if not params:
            order_instance = self.test_order_service.test_create()
            music_instance = self.test_music_service.test_create()

            params = dict()
            params['order_seq'] = order_instance['seq']
            params['music_seq'] = music_instance['seq']
            params['status'] = OrderProduct.StatusChoice.PAID.value
            params['price'] = music_instance['price']
            params['paid_at'] = datetime.datetime.now()

        print('params')
        print(params)

        serializer = self.order_product_service.create(params)

        print('serializer')
        print(json.dumps(serializer.data, ensure_ascii=False))

        return serializer.data

    def test_modify(self, path_param=None, modify_params=None):
        if not path_param:
            path_param = dict()
            path_param['seq'] = 0

        if not modify_params:
            modify_params = dict()
            modify_params[''] = None

        print('path_param')
        print(path_param)
        print('modify_params')
        print(modify_params)

        serializer = self.order_product_service.modify(
            path_param=path_param,
            params=modify_params,
            partial=True)

        print('serializer')
        print(json.dumps(serializer.data, ensure_ascii=False))

        return serializer.data

    def test_select(self, params=None):
        if not params:
            instance = self.test_create()

            params = dict()
            params['seq'] = instance['seq']

        print('params')
        print(params)

        serializer = self.order_product_service.select(path_param=params)

        print('serializer')
        print(json.dumps(serializer.data, ensure_ascii=False))

        return serializer.data

    def test_select_model(self, params=None):
        if not params:
            instance = self.test_create()

            params = dict()
            params['seq'] = instance['seq']

        print('params')
        print(params)

        model = self.order_product_service.select_model(path_param=params)

        print('model')
        print(json.dumps(model_to_dict(model), ensure_ascii=False, cls=DjangoJSONEncoder))

        return model

    def test_select_all(self, params=None):
        print('params')
        print(params)

        serializer = self.order_product_service.select_all(params=params)

        print('serializer')
        print(json.dumps(serializer.data, ensure_ascii=False))

        return serializer.data

    def test_select_all_model(self, params=None):
        print('params')
        print(params)

        models = self.order_product_service.select_all_model(params=params)

        print('models')
        print(json.dumps(list(models.values()), ensure_ascii=False, cls=DjangoJSONEncoder))

        return models
