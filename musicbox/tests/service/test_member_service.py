import json

import pytest
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import QuerySet
from django.forms import model_to_dict
from django.test import TestCase

from _musicbox.containers import Services
from member.models.member import Member
from tests.sample_data import member_sample


@pytest.mark.django_db
class TestMemberService(TestCase):
    """
    회원 서비스 테스트 코드
    """
    member_service = Services.member_service()

    @pytest.mark.skip
    def test_crud(self):
        print('--create--')
        instance = self.test_create()

        path_param = {'seq': instance['seq']}

        print('--select--')
        self.test_select(params=path_param)

        print('--select_model--')
        self.test_select_model(params=path_param)

        print('--modify--')
        self.test_modify(path_param=path_param, modify_params={'gender': Member.GenderChoice.F.value})

        print('--select_all--')
        self.test_select_all(params={'page':1})

        print('--select_all_model--')
        self.test_select_all_model(params={'page_size':1})

    @pytest.mark.skip
    def test_cycle(self):
        print('--create--')
        instance = self.test_register()

        path_param = {'seq': instance['seq']}

        print('--select--')
        self.test_select(params=path_param)

        print('--leave--')
        self.test_leave(path_param)

    @pytest.mark.skip
    def test_register(self, params=None):
        if not params:
            params = member_sample.get_register_sample()

        print('params')
        print(params)

        serializer = self.member_service.register(params)

        print('serializer')
        print(json.dumps(serializer.data, ensure_ascii=False))

        return serializer.data

    @pytest.mark.skip
    def test_leave(self, path_param=None):
        if not path_param:
            instance = self.test_create()

            path_param = dict()
            path_param['seq'] = instance['seq']

        print('path_param')
        print(path_param)

        serializer = self.member_service.leave(path_param=path_param)

        print('serializer')
        print(json.dumps(serializer.data, ensure_ascii=False))

    @pytest.mark.skip
    def test_create(self, params=None):
        if not params:
            params = dict()
            params['username'] = 'mem1'
            params['email'] = 'bomig92@gmail.com'
            params['password'] = 'test1234'
            params['gender'] = Member.GenderChoice.N.value
            params['birthday'] = '20010308'
            params['tag'] = Member.TagChoice.BASIC_USER.value

        print('params')
        print(params)

        serializer = self.member_service.create(params)

        print('serializer')
        print(json.dumps(serializer.data, ensure_ascii=False))

        return serializer.data

    @pytest.mark.skip
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

        serializer = self.member_service.modify(
            path_param=path_param,
            params=modify_params,
            partial=True)

        print('serializer')
        print(json.dumps(serializer.data, ensure_ascii=False))

        return serializer.data

    @pytest.mark.skip
    def test_select(self, params=None):
        if not params:
            instance = self.test_create()

            params = dict()
            params['seq'] = instance['seq']

        print('params')
        print(params)

        serializer = self.member_service.select(path_param=params)

        print('serializer')
        print(json.dumps(serializer.data, ensure_ascii=False))

        return serializer.data

    @pytest.mark.skip
    def test_select_model(self, params=None):
        if not params:
            instance = self.test_create()

            params = dict()
            params['seq'] = instance['seq']

        print('params')
        print(params)

        model = self.member_service.select_model(path_param=params)

        print('model')
        print(json.dumps(model_to_dict(model), ensure_ascii=False, cls=DjangoJSONEncoder))

        return model

    @pytest.mark.skip
    def test_select_all(self, params=None):
        print('params')
        print(params)

        serializer = self.member_service.select_all(params=params)

        print('serializer')
        print(json.dumps(serializer.data, ensure_ascii=False))

        return serializer.data

    @pytest.mark.skip
    def test_select_all_model(self, params=None):
        print('params')
        print(params)

        models = self.member_service.select_all_model(params=params)

        print('models')
        if isinstance(models, QuerySet):
            print(json.dumps(list(models.values()), ensure_ascii=False, cls=DjangoJSONEncoder))
        else:
            print(json.dumps([model_to_dict(item) for item in models], ensure_ascii=False, cls=DjangoJSONEncoder))

        return models
