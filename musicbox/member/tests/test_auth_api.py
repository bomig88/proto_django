import json

import pytest

from django.test import TestCase

from member.tests.test_member_service import TestMemberService


@pytest.mark.django_db
class TestAuthApi(TestCase):
    """
    회원 API 테스트 코드
    """
    test_member_service = TestMemberService()

    def test_api(self):
        self.test_api_token_verify()
        self.test_api_logout()

    def test_api_login(self, params):
        response = self.api_client.post('/auth/login', params, format='json')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

        return response.data['data']['auth']['access_token']

    def test_api_logout(self):
        response = self.api_client.post('/auth/logout')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

    def test_api_token_verify(self):
        response = self.api_client.post('/auth/token/verify', {'access_token': self.access_token}, format='json')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

        return response.data

    def test_api_token_refresh(self):
        response = self.api_client.post(f'/auth/token/refresh', {'refresh_token': self.refresh_token}, format='json')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))
