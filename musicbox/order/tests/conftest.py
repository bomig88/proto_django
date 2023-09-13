import pytest
from rest_framework.test import APIClient


@pytest.fixture(scope="class", autouse=True)
def api_client(request):
    request.cls.api_client = APIClient()
