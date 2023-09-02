
from django.test import TestCase

from _musicbox.containers import Services


class TestContentTestService(TestCase):
    content_test_service = Services.content_test_service()

    def test_t(self):
        print(self.content_test_service.hello('content'))
