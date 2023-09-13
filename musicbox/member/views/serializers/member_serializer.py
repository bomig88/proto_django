from rest_framework import serializers

from core.base.swagger_response_serializer import ResponseSerializer
from member.filters.member_filter import MemberFilter
from member.models.member import Member


class MemberSerializer01:
    class Default(serializers.ModelSerializer):
        class Meta:
            model = Member
            fields = '__all__'
            ref_name = __qualname__

    class List(serializers.ModelSerializer):
        class Meta:
            model = Member
            fields = '__all__'
            ref_name = __qualname__

    class Detail(serializers.ModelSerializer):
        class Meta:
            model = Member
            fields = '__all__'
            ref_name = __qualname__

    class Field(serializers.Serializer):
        @staticmethod
        def seq(required=True):
            seq = serializers.IntegerField(
                required=required,
                help_text=Member.seq.field.help_text
            )
            return seq

        @staticmethod
        def username(required=True):
            username = serializers.CharField(
                required=required,
                help_text=Member.username.field.help_text
            )
            return username

        @staticmethod
        def email(required=True):
            email = serializers.CharField(
                required=required,
                help_text=Member.email.field.help_text
            )
            return email

        @staticmethod
        def sch_start_create_dt(required=True):
            sch_start_create_dt = serializers.DateTimeField(
                required=required,
                help_text=MemberFilter.base_filters['sch_start_create_dt'].field.help_text
            )
            return sch_start_create_dt

        @staticmethod
        def sch_end_create_dt(required=True):
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
    class GetParam(serializers.Serializer):
        seq = MemberSerializer01.Field.seq(False)
        username = MemberSerializer01.Field.username(False)
        email = MemberSerializer01.Field.email(False)
        sch_start_create_dt = MemberSerializer01.Field.sch_start_create_dt(False)
        sch_end_create_dt = MemberSerializer01.Field.sch_end_create_dt(False)
        ordering = MemberSerializer01.Field.ordering(False)

        class Meta:
            ref_name = __qualname__

    class GetResponse(serializers.Serializer):
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
