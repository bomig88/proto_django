from rest_framework import serializers

from content.filters.artist_additional_info_filter import ArtistAdditionalInfoFilter
from content.models.artist_additional_info import ArtistAdditionalInfo
from core.base.swagger_response_serializer import ResponseSerializer


class ArtistAdditionalInfoSerializer01:
    """
    Swagger 아티스트 추가 정보 Serializer
    """
    class Default(serializers.ModelSerializer):

        class Meta:
            model = ArtistAdditionalInfo
            fields = '__all__'
            ref_name = __qualname__

    class List(serializers.ModelSerializer):
        class Meta:
            model = ArtistAdditionalInfo
            fields = '__all__'
            ref_name = __qualname__

    class Detail(serializers.ModelSerializer):
        class Meta:
            model = ArtistAdditionalInfo
            fields = '__all__'
            ref_name = __qualname__

    class Field(serializers.Serializer):
        @staticmethod
        def seq(required=True):
            seq = serializers.IntegerField(
                required=required,
                help_text=ArtistAdditionalInfo.seq.field.help_text
            )
            return seq

        @staticmethod
        def sch_start_create_dt(required=True):
            sch_start_create_dt = serializers.DateTimeField(
                required=required,
                help_text=ArtistAdditionalInfoFilter.base_filters['sch_start_create_dt'].field.help_text
            )
            return sch_start_create_dt

        @staticmethod
        def sch_end_create_dt(required=True):
            sch_end_create_dt = serializers.DateTimeField(
                required=required,
                help_text=ArtistAdditionalInfoFilter.base_filters['sch_end_create_dt'].field.help_text
            )
            return sch_end_create_dt

        @staticmethod
        def ordering(required=False):
            ordering = serializers.ChoiceField(
                choices=list(ArtistAdditionalInfoFilter.base_filters['ordering'].param_map.values()),
                required=required,
                help_text=ArtistAdditionalInfoFilter.base_filters['ordering'].field.help_text
            )
            return ordering


class ArtistAdditionalInfoSerializer02:
    """
    Swagger 아티스트 추가 정보 Serializer
    """
    class GetParam(serializers.Serializer):
        seq = ArtistAdditionalInfoSerializer01.Field.seq(False)
        sch_start_create_dt = ArtistAdditionalInfoSerializer01.Field.sch_start_create_dt(False)
        sch_end_create_dt = ArtistAdditionalInfoSerializer01.Field.sch_end_create_dt(False)
        ordering = ArtistAdditionalInfoSerializer01.Field.ordering(False)

        class Meta:
            ref_name = __qualname__

    class GetResponse(serializers.Serializer):
        artist_additional_infos = serializers.ListField(
            child=ArtistAdditionalInfoSerializer01.List(),
            required=False,
            help_text="아티스트 추가 정보 목록"
        )

        class Meta:
            ref_name = __qualname__

    class DetailGetResponse(ResponseSerializer):
        class DetailGetResponseData(serializers.Serializer):
            artist_additional_info = ArtistAdditionalInfoSerializer01.Detail(help_text="아티스트 추가 정보")

            class Meta:
                ref_name = __qualname__

        data = DetailGetResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__
