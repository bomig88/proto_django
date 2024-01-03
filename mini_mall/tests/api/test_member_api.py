import pytest

from django.test import TestCase

from member.models.member import Member


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client")
class TestMemberApi(TestCase):
    """
    회원 API 테스트 코드
    """
    def test_api(self):
        #### register test start
        basic_user_params = dict()
        basic_user_params['username'] = 'regit_api'
        basic_user_params['password'] = 'test1234'
        basic_user_params['birthday'] = '20000101'
        basic_user_params['gender'] = Member.GenderChoice.F.value
        basic_user_params['email'] = 'regit_api_981@gmail.com'
        basic_user_params['tag'] = Member.TagChoice.BASIC_USER.value

        # register
        basic_user_response = self.api_client.post('/members/register', basic_user_params, format='json')
        print(f'basic_user register.status_code = {basic_user_response.status_code}')
        print('basic_user register response.data', basic_user_response.data, end='\n')
        assert basic_user_response.status_code == 200
        assert basic_user_response.data['success'] == True

        manager_params = dict()
        manager_params['username'] = 'regit2'
        manager_params['password'] = 'test1234'
        manager_params['birthday'] = '20000101'
        manager_params['gender'] = Member.GenderChoice.M.value
        manager_params['email'] = 'regit2@gmail.com'
        manager_params['tag'] = Member.TagChoice.MANAGER.value

        # register
        manager_response = self.api_client.post('/members/register', manager_params, format='json')
        print(f'manager register.status_code = {manager_response.status_code}')
        print('manager register response.data', manager_response.data, end='\n')
        assert manager_response.status_code == 200
        assert manager_response.data['success'] == True

        super_manager_params = dict()
        super_manager_params['username'] = 'regit3'
        super_manager_params['password'] = 'test1234'
        super_manager_params['birthday'] = '20000101'
        super_manager_params['gender'] = Member.GenderChoice.N.value
        super_manager_params['email'] = 'regit3@gmail.com'
        super_manager_params['tag'] = Member.TagChoice.SUPER_MANAGER.value

        # register
        super_manager_response = self.api_client.post('/members/register', super_manager_params, format='json')
        print(f'super_manager register.status_code = {super_manager_response.status_code}')
        print('super_manager register response.data', super_manager_response.data, end='\n')
        assert super_manager_response.status_code == 200
        assert super_manager_response.data['success'] == True

        ##### register test complete

        basic_user_seq = basic_user_response.data['data']['member']['seq']

        # select
        response = self.api_client.get(f'/members/{basic_user_seq}')
        print(f'select.status_code = {response.status_code}')
        print('select response.data', response.data, end='\n')
        assert response.status_code == 200
        assert response.data['success'] == True
        assert response.data['data']['member']['seq'] == basic_user_seq

        # select_all
        response = self.api_client.get('/members?page=1')
        print(f'select_all.status_code = {response.status_code}')
        print('select_all response.data', response.data, end='\n')
        assert response.status_code == 200
        assert response.data['success'] == True
        assert len(response.data['data']['members']) > 0

        # leave
        response = self.api_client.post(f'/members/{basic_user_seq}/leave')
        print(f'leave.status_code = {response.status_code}')
        print('leave response.data', response.data, end='\n')
        assert response.status_code == 200
        assert response.data['success'] == True

        from config.containers import Services
        leave_member_serializer = Services.member_service().select(path_param={'seq': basic_user_seq})
        print('leave_member_serializer', leave_member_serializer.data)
        assert leave_member_serializer.data.get('status') == Member.StatusChoice.LEAVE.value
