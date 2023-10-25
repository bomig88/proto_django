import json

from django.test import TestCase

import pytest

from content.tests.test_album_service import TestAlbumService


@pytest.mark.django_db
class TestAlbumApi(TestCase):
    """
    앨범 API 테스트 코드
    """
    test_album_service = TestAlbumService()

    def test_api(self):
        self.test_album_service.test_crud()
        self.test_api_select_all()
        self.test_api_select()

    def test_api_select_all(self):
        response = self.api_client.get('/contents/albums?page=1')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

    def test_api_select(self):
        response = self.api_client.get('/contents/albums/1')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))
