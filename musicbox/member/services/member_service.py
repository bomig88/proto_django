import datetime

from core.base.base_service import BaseService
from member.filters.member_filter import MemberFilter
from member.models.member import Member
from member.serializers.member_serializer import MemberSerializer, MemberDetailSerializer, MemberListSerializer


class MemberService(BaseService):
    """
    회원 서비스
    """
    queryset_list = Member.objects.all()
    queryset_detail = Member.objects.all()
    serializer = MemberSerializer
    serializer_list = MemberListSerializer
    serializer_detail = MemberDetailSerializer
    filter_set_class = MemberFilter

    def create(self, params: dict):
        """
        회원 모델 생성
        Args:
            params: 등록한 모델의 구성 정보
        Returns:
            모델 Serializer
        """
        params['status'] = Member.StatusChoice.JOIN.value
        params['is_active'] = True

        return super().create(params)

    def register(self, params: dict):
        """
        회원 가입
        Args:
            params: 등록할 모델의 구성 정보
        Returns:
            모델 Serializer
        Raises:
            Exception
        """
        if 'username' in params and 'password' in params and 'email' in params \
                and 'birthday' in params and 'gender' in params:

            return self.create(params)

        else:
            raise Exception('필수 파라미터를 확인해주세요.')

    def leave(self, path_param: dict, params: dict = None):
        """
        회원 탈퇴
        Args:
            path_param: 회원 pk 정보
            params: 변경 사항
        Returns:
            변경된 모델 Serializer
        """
        if not params:
            params = dict()

        params['status'] = Member.StatusChoice.LEAVE.value
        params['leave_at'] = datetime.datetime.now()

        return self.modify(path_param, params, partial=True)
