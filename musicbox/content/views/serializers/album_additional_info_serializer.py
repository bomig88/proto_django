from rest_framework import serializers

from content.filters.album_additional_info_filter import AlbumAdditionalInfoFilter
from content.models.album_additional_info import AlbumAdditionalInfo
from core.base.swagger_response_serializer import ResponseSerializer


class AlbumAdditionalInfoSerializer01:
    class Default(serializers.ModelSerializer):

        class Meta:
            model = AlbumAdditionalInfo
            fields = '__all__'
            ref_name = __qualname__

    class List(serializers.ModelSerializer):
        class Meta:
            model = AlbumAdditionalInfo
            fields = '__all__'
            ref_name = __qualname__

    class Detail(serializers.ModelSerializer):
        class Meta:
            model = AlbumAdditionalInfo
            fields = '__all__'
            ref_name = __qualname__

    class Field(serializers.Serializer):
        @staticmethod
        def seq(required=True):
            seq = serializers.IntegerField(
                required=required,
                help_text=AlbumAdditionalInfo.seq.field.help_text
            )
            return seq

        @staticmethod
        def sch_start_create_dt(required=True):
            sch_start_create_dt = serializers.DateTimeField(
                required=required,
                help_text=AlbumAdditionalInfoFilter.base_filters['sch_start_create_dt'].field.help_text
            )
            return sch_start_create_dt

        @staticmethod
        def sch_end_create_dt(required=True):
            sch_end_create_dt = serializers.DateTimeField(
                required=required,
                help_text=AlbumAdditionalInfoFilter.base_filters['sch_end_create_dt'].field.help_text
            )
            return sch_end_create_dt

        @staticmethod
        def ordering(required=False):
            ordering = serializers.ChoiceField(
                choices=list(AlbumAdditionalInfoFilter.base_filters['ordering'].param_map.values()),
                required=required,
                help_text=AlbumAdditionalInfoFilter.base_filters['ordering'].field.help_text
            )
            return ordering


class AlbumAdditionalInfoSerializer02:
    class GetParam(serializers.Serializer):
        seq = AlbumAdditionalInfoSerializer01.Field.seq(False)
        sch_start_create_dt = AlbumAdditionalInfoSerializer01.Field.sch_start_create_dt(False)
        sch_end_create_dt = AlbumAdditionalInfoSerializer01.Field.sch_end_create_dt(False)
        ordering = AlbumAdditionalInfoSerializer01.Field.ordering(False)

        class Meta:
            ref_name = __qualname__

    class GetResponse(serializers.Serializer):
        album_additional_infos = serializers.ListField(
            child=AlbumAdditionalInfoSerializer01.List(),
            required=False,
            help_text="앨범 추가 정보 목록"
        )

        class Meta:
            ref_name = __qualname__

    class DetailGetResponse(ResponseSerializer):
        class DetailGetResponseData(serializers.Serializer):
            album_additional_info = AlbumAdditionalInfoSerializer01.Detail(help_text="앨범 추가 정보")

            class Meta:
                ref_name = __qualname__

        data = DetailGetResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__
