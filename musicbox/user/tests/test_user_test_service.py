
from django.test import TestCase

from _musicbox.containers import Services


class TestUserTestService(TestCase):
    user_test_service = Services.user_test_service()

    def test_t(self):
        print(self.user_test_service.hello('user'))
