import json

import pytest

from django.test import TestCase

from content.tests.test_music_service import TestMusicService


@pytest.mark.django_db
class TestMusicApi(TestCase):
    """
    곡 API 테스트 코드
    """
    test_music_service = TestMusicService()

    def test_api(self):
        self.test_music_service.test_crud()
        self.test_api_select_all()
        self.test_api_select()

    def test_api_select_all(self):
        response = self.api_client.get('/contents/musics?page=1')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))

    def test_api_select(self):
        response = self.api_client.get('/contents/musics/1')
        print(f'response.status_code = {response.status_code}')
        assert response.status_code == 200

        print('response.data')
        print(json.dumps(response.data, ensure_ascii=False))
