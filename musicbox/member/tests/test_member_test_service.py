
from django.test import TestCase

from _musicbox.containers import Services


class TestMemberTestService(TestCase):
    member_test_service = Services.member_test_service()

    def test_t(self):
        print(self.member_test_service.hello('member'))
