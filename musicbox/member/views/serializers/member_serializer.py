from rest_framework import serializers

from core.base.swagger_response_serializer import ResponseSerializer, PagingResponseSerializer, PagingFieldSerializer
from member.filters.member_filter import MemberFilter
from member.models.member import Member


class MemberSerializer01:
    """
    Swagger 회원 Serializer
    """
    class Default(serializers.ModelSerializer):
        class Meta:
            model = Member
            exclude = [
                Member.password.field.name,
                Member.groups.field.name,
                Member.user_permissions.field.name,
            ]
            ref_name = __qualname__

    class List(serializers.ModelSerializer):
        class Meta:
            model = Member
            exclude = [
                Member.password.field.name,
                Member.groups.field.name,
                Member.user_permissions.field.name,
            ]
            ref_name = __qualname__

    class Detail(serializers.ModelSerializer):
        class Meta:
            model = Member
            exclude = [
                Member.password.field.name,
                Member.groups.field.name,
                Member.user_permissions.field.name,
            ]
            ref_name = __qualname__

    class Field(serializers.Serializer):
        @staticmethod
        def seq(required=False):
            seq = serializers.IntegerField(
                required=required,
                help_text=Member.seq.field.help_text
            )
            return seq

        @staticmethod
        def username(required=False):
            username = serializers.CharField(
                required=required,
                help_text=Member.username.field.help_text
            )
            return username

        @staticmethod
        def password(required=False):
            password = serializers.CharField(
                required=required,
                help_text=Member.password.field.help_text
            )
            return password

        @staticmethod
        def email(required=False):
            email = serializers.CharField(
                required=required,
                help_text=Member.email.field.help_text
            )
            return email

        @staticmethod
        def gender(required=False):
            gender = serializers.ChoiceField(
                choices=tuple(Member.GenderChoice.choices),
                required=required,
                help_text=f'{Member.gender.field.help_text} \ {str(Member.GenderChoice.choices)}'
            )
            return gender

        @staticmethod
        def status(required=False):
            status = serializers.ChoiceField(
                choices=tuple(Member.StatusChoice.choices),
                required=required,
                help_text=f'{Member.status.field.help_text} \ {str(Member.StatusChoice.choices)}'
            )
            return status

        @staticmethod
        def tag(required=False):
            tag = serializers.ChoiceField(
                choices=tuple(Member.TagChoice.choices),
                required=required,
                help_text=f'{Member.tag.field.help_text} \ {str(Member.TagChoice.choices)}'
            )
            return tag

        @staticmethod
        def birthday(required=False):
            birthday = serializers.CharField(
                required=required,
                help_text=Member.birthday.field.help_text
            )
            return birthday

        @staticmethod
        def sch_start_create_dt(required=False):
            sch_start_create_dt = serializers.DateTimeField(
                required=required,
                help_text=MemberFilter.base_filters['sch_start_create_dt'].field.help_text
            )
            return sch_start_create_dt

        @staticmethod
        def sch_end_create_dt(required=False):
            sch_end_create_dt = serializers.DateTimeField(
                required=required,
                help_text=MemberFilter.base_filters['sch_end_create_dt'].field.help_text
            )
            return sch_end_create_dt

        @staticmethod
        def ordering(required=False):
            ordering = serializers.ChoiceField(
                choices=list(MemberFilter.base_filters['ordering'].param_map.values()),
                required=required,
                help_text=MemberFilter.base_filters['ordering'].field.help_text
            )
            return ordering


class MemberSerializer02:
    """
    Swagger 회원 Serializer
    """
    class GetParam(serializers.Serializer):
        seq = MemberSerializer01.Field.seq(required=False)
        username = MemberSerializer01.Field.username(required=False)
        email = MemberSerializer01.Field.email(required=False)
        status = MemberSerializer01.Field.status(required=False)
        tag = MemberSerializer01.Field.tag(required=False)
        sch_start_create_dt = MemberSerializer01.Field.sch_start_create_dt(required=False)
        sch_end_create_dt = MemberSerializer01.Field.sch_end_create_dt(required=False)

        page = PagingFieldSerializer.page(required=False)
        page_size = PagingFieldSerializer.page_size(required=False)

        ordering = MemberSerializer01.Field.ordering(required=False)

        class Meta:
            ref_name = __qualname__

    class GetResponse(PagingResponseSerializer):
        members = serializers.ListField(
            child=MemberSerializer01.List(),
            required=False,
            help_text="회원 목록"
        )

        class Meta:
            ref_name = __qualname__

    class DetailGetResponse(ResponseSerializer):
        class DetailGetResponseData(serializers.Serializer):
            member = MemberSerializer01.Detail(help_text="회원")

            class Meta:
                ref_name = __qualname__

        data = DetailGetResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__

    class RegisterPostRequest(serializers.Serializer):
        username = MemberSerializer01.Field.username(required=True)
        password = MemberSerializer01.Field.password(required=True)
        email = MemberSerializer01.Field.email(required=True)
        gender = MemberSerializer01.Field.gender(required=True)
        birthday = MemberSerializer01.Field.birthday(required=True)
        tag = MemberSerializer01.Field.tag(required=True)

        class Meta:
            ref_name = __qualname__

    class RegisterPostResponse(ResponseSerializer):

        class RegisterPostResponseData(serializers.Serializer):
            member = MemberSerializer01.Detail(help_text="등록된 회원 정보")

            class Meta:
                ref_name = __qualname__

        data = RegisterPostResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__

    class LeavePostRequest(serializers.Serializer):

        class Meta:
            ref_name = __qualname__
