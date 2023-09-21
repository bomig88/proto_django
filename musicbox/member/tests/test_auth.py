import json

import pytest
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.test import TestCase

from _musicbox.containers import Services
from core.auth.base_post_handle_authentication import BasePostHandleAuthentication
from member.models.member import Member
from member.tests.test_member_service import TestMemberService


@pytest.mark.django_db
class TestAuth(TestCase):
    """
    회원 서비스 테스트 코드
    """
    test_member_service = TestMemberService()

    def test_cycle(self):
        print('--create--')
        instance = self.test_member_service.test_register()

        path_param = {'seq': instance['seq']}

        print('--select--')
        self.test_member_service.test_select(params=path_param)

        print('--login--')
        login_param = {'username': instance['username'], 'password': 'test1234'}
        self.test_login(login_param)

    def test_login(self, params):
        response = BasePostHandleAuthentication().token(params)
        print(f'response = {response}')

        return response
