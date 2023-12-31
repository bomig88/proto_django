import pytest
from rest_framework.test import APIClient

from member.models.member import Member


@pytest.fixture(scope="class")
def api_client(request):
    username = "bomig88"
    password = "test1234"
    params = dict()
    params['username'] = username
    params['password'] = password
    params['birthday'] = '20000101'
    params['gender'] = Member.GenderChoice.F.value
    params['email'] = 'bomig@gmail.com'
    params['tag'] = Member.TagChoice.SUPER_MANAGER.value

    from config.containers import Services
    member_service = Services.member_service()
    try:
        member = member_service.select({'username': username})
    except (Exception,):
        member = member_service.register(params)

    request.cls.member_seq = member.data['seq']

    login_param = {'username': username, 'password': password}

    api_client = APIClient()

    response = api_client.post('/auth/login', login_param, format='json')
    print(f'login response.status_code = {response.status_code}')
    print('login response.data', response.data, end='\n')
    assert response.status_code == 200

    access_token = response.data['data']['auth']['access_token']
    refresh_token = response.data['data']['auth']['access_token']

    api_client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {access_token}",
        )

    request.cls.api_client = api_client
    request.cls.access_token = access_token
    request.cls.refresh_token = refresh_token
