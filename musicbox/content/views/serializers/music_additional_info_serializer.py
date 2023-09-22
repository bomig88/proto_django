from rest_framework import serializers

from content.filters.music_additional_info_filter import MusicAdditionalInfoFilter
from content.models.music_additional_info import MusicAdditionalInfo
from core.base.swagger_response_serializer import ResponseSerializer


class MusicAdditionalInfoSerializer01:
    """
    Swagger 곡 추가 정보 Serializer
    """
    class Default(serializers.ModelSerializer):

        class Meta:
            model = MusicAdditionalInfo
            fields = '__all__'
            ref_name = __qualname__

    class List(serializers.ModelSerializer):
        class Meta:
            model = MusicAdditionalInfo
            fields = '__all__'
            ref_name = __qualname__

    class Detail(serializers.ModelSerializer):
        class Meta:
            model = MusicAdditionalInfo
            fields = '__all__'
            ref_name = __qualname__

    class Field(serializers.Serializer):
        @staticmethod
        def seq(required=True):
            seq = serializers.IntegerField(
                required=required,
                help_text=MusicAdditionalInfo.seq.field.help_text
            )
            return seq

        @staticmethod
        def sch_start_create_dt(required=True):
            sch_start_create_dt = serializers.DateTimeField(
                required=required,
                help_text=MusicAdditionalInfoFilter.base_filters['sch_start_create_dt'].field.help_text
            )
            return sch_start_create_dt

        @staticmethod
        def sch_end_create_dt(required=True):
            sch_end_create_dt = serializers.DateTimeField(
                required=required,
                help_text=MusicAdditionalInfoFilter.base_filters['sch_end_create_dt'].field.help_text
            )
            return sch_end_create_dt

        @staticmethod
        def ordering(required=False):
            ordering = serializers.ChoiceField(
                choices=list(MusicAdditionalInfoFilter.base_filters['ordering'].param_map.values()),
                required=required,
                help_text=MusicAdditionalInfoFilter.base_filters['ordering'].field.help_text
            )
            return ordering


class MusicAdditionalInfoSerializer02:
    """
    Swagger 곡 추가 정보 Serializer
    """
    class GetParam(serializers.Serializer):
        seq = MusicAdditionalInfoSerializer01.Field.seq(False)
        sch_start_create_dt = MusicAdditionalInfoSerializer01.Field.sch_start_create_dt(False)
        sch_end_create_dt = MusicAdditionalInfoSerializer01.Field.sch_end_create_dt(False)
        ordering = MusicAdditionalInfoSerializer01.Field.ordering(False)

        class Meta:
            ref_name = __qualname__

    class GetResponse(serializers.Serializer):
        music_additional_infos = serializers.ListField(
            child=MusicAdditionalInfoSerializer01.List(),
            required=False,
            help_text="곡 추가 정보 목록"
        )

        class Meta:
            ref_name = __qualname__

    class DetailGetResponse(ResponseSerializer):
        class DetailGetResponseData(serializers.Serializer):
            music_additional_info = MusicAdditionalInfoSerializer01.Detail(help_text="곡 추가 정보")

            class Meta:
                ref_name = __qualname__

        data = DetailGetResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__
