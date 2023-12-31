import pytest
from django.test import TestCase

from config.containers import Services
from member.models.member import Member


@pytest.mark.django_db
class TestMemberService(TestCase):
    """
    회원 서비스 테스트 코드
    """
    member_service = Services.member_service()

    def test_crud_member(self):
        # register
        basic_user_params = dict()
        basic_user_params['username'] = 'regit1'
        basic_user_params['password'] = 'test1234'
        basic_user_params['birthday'] = '20000101'
        basic_user_params['gender'] = Member.GenderChoice.F.value
        basic_user_params['email'] = 'regit1@gmail.com'
        basic_user_params['tag'] = Member.TagChoice.BASIC_USER.value

        register_basic_user_instance = self.member_service.register(basic_user_params)
        assert register_basic_user_instance.data.get('tag') == Member.TagChoice.BASIC_USER.value

        manager_params = dict()
        manager_params['username'] = 'regit2'
        manager_params['password'] = 'test1234'
        manager_params['birthday'] = '20000101'
        manager_params['gender'] = Member.GenderChoice.M.value
        manager_params['email'] = 'regit2@gmail.com'
        manager_params['tag'] = Member.TagChoice.MANAGER.value

        register_manager_instance = self.member_service.register(manager_params)
        assert register_manager_instance.data.get('tag') == Member.TagChoice.MANAGER.value

        super_manager_params = dict()
        super_manager_params['username'] = 'regit3'
        super_manager_params['password'] = 'test1234'
        super_manager_params['birthday'] = '20000101'
        super_manager_params['gender'] = Member.GenderChoice.N.value
        super_manager_params['email'] = 'regit3@gmail.com'
        super_manager_params['tag'] = Member.TagChoice.SUPER_MANAGER.value

        register_super_manager_instance = self.member_service.register(super_manager_params)
        assert register_super_manager_instance.data.get('tag') == Member.TagChoice.SUPER_MANAGER.value

        member_seq = register_basic_user_instance.data.get('seq')
        path_param = {'seq': member_seq}

        # select
        select_serializer = self.member_service.select(path_param=path_param)
        assert select_serializer.data.get('seq') == member_seq

        # select_all
        serializer = self.member_service.select_all(params=None)
        assert len(serializer.data) > 0

        # select_all_model
        models = self.member_service.select_all_model(params=None)
        assert models

        # modify
        modify_params = {'gender': Member.GenderChoice.M.value}
        modify_member_serializer = self.member_service.modify(
            path_param=path_param,
            params=modify_params,
            partial=True)
        assert modify_member_serializer.data.get('gender') == Member.GenderChoice.M.value

        # select_model
        member_model = self.member_service.select_model(path_param=path_param)
        assert member_model.gender == Member.GenderChoice.M.value

        # leave
        serializer = self.member_service.leave(path_param=path_param)
        assert serializer.data.get('status') == Member.StatusChoice.LEAVE.value
