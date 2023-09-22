import json

import pytest

from django.test import TestCase

from content.tests.test_artist_service import TestArtistService


@pytest.mark.django_db
class TestArtistApi(TestCase):
    """
    아티스트 API 테스트 코드
    """
    test_artist_service = TestArtistService()

    def test_api(self):
        self.test_artist_service.test_crud()
        self.test_api_select_all()
        self.test_api_select()

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
