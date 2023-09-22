import pytest
from rest_framework.test import APIClient

from member.models.member import Member


@pytest.fixture(scope="function", autouse=True)
def api_client(request):
    params = dict()
    params['username'] = 'regit1'
    params['password'] = 'test1234'
    params['birthday'] = '20000101'
    params['gender'] = Member.GenderChoice.F.value
    params['email'] = 'bomig@gmail.com'

    from _musicbox.containers import Services
    member = Services.member_service().register(params)
    request.cls.member_seq = member.data['seq']

    login_param = {'username': params['username'], 'password': params['password']}

    api_client = APIClient()

    response = api_client.post('/auth/login', login_param, format='json')
    print(f'login response.status_code = {response.status_code}')
    assert response.status_code == 200

    print('response.data')
    print(response.data)

    access_token = response.data['data']['auth']['access_token']
    refresh_token = response.data['data']['auth']['access_token']

    api_client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {access_token}",
        )

    request.cls.api_client = api_client
    request.cls.access_token = access_token
    request.cls.refresh_token = refresh_token
