from core.base.base_service import BaseService
from member.filters.member_filter import MemberFilter
from member.models.member import Member
from member.serializers.member_serializer import MemberSerializer, MemberDetailSerializer, MemberListSerializer


class MemberService(BaseService):
    queryset_list = Member.objects.all()
    queryset_detail = Member.objects.all()
    serializer = MemberSerializer
    serializer_list = MemberListSerializer
    serializer_detail = MemberDetailSerializer
    filter_set_class = MemberFilter

    def create(self, params: dict):
        params['status'] = Member.StatusChoice.JOIN.value
        params['is_active'] = True

        return super().create(params)
