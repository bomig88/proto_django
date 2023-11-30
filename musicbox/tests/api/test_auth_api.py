import json

import pytest

from django.test import TestCase


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client")
class TestAuthApi(TestCase):
    """
    회원 API 테스트 코드
    """
    def test_api_token_verify(self):
        response = self.api_client.post('/auth/token/verify', {'access_token': self.access_token}, format='json')
        print(f'token_verify.status_code = {response.status_code}')
        print('token_verify response.data', response.data, end='\n')
        assert response.status_code == 200
        assert response.data['success'] == True

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

        return response.data

    @pytest.mark.skip
    def test_api_token_refresh(self):
        response = self.api_client.post(f'/auth/token/refresh', {'refresh_token': self.refresh_token}, format='json')
        print(f'token_refresh.status_code = {response.status_code}')
        print('token_refresh response.data', response.data, end='\n')
        assert response.status_code == 200
        assert response.data['success'] == True

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

    def test_api_logout(self):
        response = self.api_client.post('/auth/logout')
        print(f'logout.status_code = {response.status_code}')
        print('logout response.data', response.data, end='\n')
        assert response.status_code == 200
        assert response.data['success'] == True

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))
