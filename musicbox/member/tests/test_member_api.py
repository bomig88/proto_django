import json

import pytest

from django.test import TestCase

from member.tests.test_member_service import TestMemberService


@pytest.mark.django_db
class TestMemberApi(TestCase):
    """
    회원 API 테스트 코드
    """
    test_member_service = TestMemberService()

    def test_api(self):
        self.test_member_service.test_crud()
        self.test_api_select_all()
        self.test_api_select()

    def test_cycle_api(self):
        data = self.test_api_register(TestMemberService.get_register_sample())
        self.test_api_leave(seq=data['data']['member']['seq'])

    def test_api_select_all(self):
        response = self.api_client.get('/members/')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

    def test_api_select(self):
        response = self.api_client.get('/members/1')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

    def test_api_register(self, params):
        response = self.api_client.post('/members/register', params, format='json')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

        return response.data

    def test_api_leave(self, seq):
        response = self.api_client.post(f'/members/{seq}/leave')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))
