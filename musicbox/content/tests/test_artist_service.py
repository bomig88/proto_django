import json
import random

import pytest
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.test import TestCase

from _musicbox.containers import Services
from content.tests.test_artist_additional_info_service import TestArtistAdditionalInfoService


@pytest.mark.django_db
class TestArtistService(TestCase):
    artist_service = Services.artist_service()
    test_artist_additional_info_service = TestArtistAdditionalInfoService()

    def test_crud(self):
        print('--create--')
        instance = self.test_create()

        path_param = {'seq': instance['seq']}

        print('--select--')
        self.test_select(params=path_param)

        print('--select_model--')
        self.test_select_model(params=path_param)

        print('--modify--')
        self.test_modify(path_param=path_param, modify_params={'name': f'{instance["name"]}_test!'})

        print('--select_all--')
        self.test_select_all(params={})

        print('--select_all_model--')
        self.test_select_all_model(params={})

    def test_api(self):
        self.test_crud()
        self.test_api_select_all()
        self.test_api_select()

    def test_create(self, params=None):
        if not params:
            params = dict()
            params['name'] = f'아이브_{random.randint(1,100)}'

            artist_additional_info_seq_instance = self.test_artist_additional_info_service.test_create()
            params['artist_additional_info_seq'] = artist_additional_info_seq_instance['seq']

        print('params')
        print(params)

        serializer = self.artist_service.create(params)

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

        serializer = self.artist_service.modify(
            path_param=path_param,
            params=modify_params,
            partial=False)

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

        serializer = self.artist_service.select(path_param=params)

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

        model = self.artist_service.select_model(path_param=params)

        print('model')
        print(json.dumps(model_to_dict(model), ensure_ascii=False, cls=DjangoJSONEncoder))

        return model

    def test_select_all(self, params=None):
        print('params')
        print(params)

        serializer = self.artist_service.select_all(params=params)

        print('serializer')
        print(json.dumps(serializer.data, ensure_ascii=False))

        return serializer.data

    def test_select_all_model(self, params=None):
        print('params')
        print(params)

        models = self.artist_service.select_all_model(params=params)

        print('models')
        print(json.dumps(list(models.values()), ensure_ascii=False, cls=DjangoJSONEncoder))

        return models

    def test_api_select_all(self):
        response = self.api_client.get('/contents/artists')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

    def test_api_select(self):
        response = self.api_client.get('/contents/artists/1')
        assert response.status_code == 200

        print(f'response.status_code = {response.status_code}')
        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))
