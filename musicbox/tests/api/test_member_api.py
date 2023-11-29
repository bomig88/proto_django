import json

import pytest

from django.test import TestCase
from tests.sample_data import member_sample


@pytest.mark.django_db
class TestMemberApi(TestCase):
    """
    회원 API 테스트 코드
    """
    @pytest.mark.skip
    def test_api(self):
        data = self.test_api_register(member_sample.get_register_manager_sample())
        seq = data['data']['member']['seq']
        self.test_api_select_all()
        self.test_api_select(seq)
        self.test_api_leave(seq=seq)

    @pytest.mark.skip
    def test_api_select_all(self):
        response = self.api_client.get('/members?page=1')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

    @pytest.mark.skip
    def test_api_select(self, seq):
        response = self.api_client.get(f'/members/{seq}')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

    @pytest.mark.skip
    def test_api_register(self, params):
        response = self.api_client.post('/members/register', params, format='json')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

        return response.data

    @pytest.mark.skip
    def test_api_leave(self, seq):
        response = self.api_client.post(f'/members/{seq}/leave')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))
