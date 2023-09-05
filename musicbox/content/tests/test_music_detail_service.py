import json

import pytest
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.test import TestCase

from _musicbox.containers import Services
from content.tests.test_music_service import TestMusicService


@pytest.mark.django_db
class TestMusicDetailService(TestCase):
    music_detail_service = Services.music_detail_service()
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
        self.test_modify(path_param=path_param, modify_params={'original_artist': f'{instance["composer"]}'})

        print('--select_all--')
        self.test_select_all(params={})

        print('--select_all_model--')
        self.test_select_all_model(params={})

    def test_create(self, params=None):
        if not params:
            params = dict()
            params['name'] = '아이브'
            params['composer'] = '아이브'
            params['lyricist'] = '아이브'
            params['original_artist'] = None
            params['lyrics'] = """
            가사를 이케 요케 저케 그러케
            마구 넣어 주면 됩니다
            참 쉽죵
            """

            instance = self.test_music_service.test_create()
            params['music_seq'] = instance['seq']

        print('params')
        print(params)

        serializer = self.music_detail_service.create(params)

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

        serializer = self.music_detail_service.modify(
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

        serializer = self.music_detail_service.select(path_param=params)

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

        model = self.music_detail_service.select_model(path_param=params)

        print('model')
        print(json.dumps(model_to_dict(model), ensure_ascii=False, cls=DjangoJSONEncoder))

        return model

    def test_select_all(self, params=None):
        print('params')
        print(params)

        serializer = self.music_detail_service.select_all(params=params)

        print('serializer')
        print(json.dumps(serializer.data, ensure_ascii=False))

        return serializer.data

    def test_select_all_model(self, params=None):
        print('params')
        print(params)

        models = self.music_detail_service.select_all_model(params=params)

        print('models')
        print(json.dumps(list(models.values()), ensure_ascii=False, cls=DjangoJSONEncoder))

        return models
