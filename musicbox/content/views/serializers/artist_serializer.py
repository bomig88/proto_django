from rest_framework import serializers

from content.filters.artist_filter import ArtistFilter
from content.models.artist import Artist
from content.views.serializers.artist_additional_info_serializer import ArtistAdditionalInfoSerializer01
from core.base.swagger_response_serializer import ResponseSerializer, PagingResponseSerializer, PagingFieldSerializer


class ArtistSerializer01:
    """
    Swagger 아티스트 Serializer
    """
    class Default(serializers.ModelSerializer):

        class Meta:
            model = Artist
            fields = '__all__'
            ref_name = __qualname__

    class List(serializers.ModelSerializer):
        class Meta:
            model = Artist
            fields = '__all__'
            ref_name = __qualname__

    class Detail(serializers.ModelSerializer):
        artist_additional_info = ArtistAdditionalInfoSerializer01.Detail(many=False)

        class Meta:
            model = Artist
            fields = '__all__'
            ref_name = __qualname__

    class Field(serializers.Serializer):
        @staticmethod
        def seq(required=True):
            seq = serializers.IntegerField(
                required=required,
                help_text=Artist.seq.field.help_text
            )
            return seq

        @staticmethod
        def name(required=True):
            name = serializers.CharField(
                required=required,
                help_text=Artist.name.field.help_text
            )
            return name

        @staticmethod
        def sch_start_create_dt(required=True):
            sch_start_create_dt = serializers.DateTimeField(
                required=required,
                help_text=ArtistFilter.base_filters['sch_start_create_dt'].field.help_text
            )
            return sch_start_create_dt

        @staticmethod
        def sch_end_create_dt(required=True):
            sch_end_create_dt = serializers.DateTimeField(
                required=required,
                help_text=ArtistFilter.base_filters['sch_end_create_dt'].field.help_text
            )
            return sch_end_create_dt

        @staticmethod
        def ordering(required=False):
            ordering = serializers.ChoiceField(
                choices=list(ArtistFilter.base_filters['ordering'].param_map.values()),
                required=required,
                help_text=ArtistFilter.base_filters['ordering'].field.help_text
            )
            return ordering


class ArtistSerializer02:
    """
    Swagger 아티스트 Serializer
    """
    class GetParam(serializers.Serializer):
        seq = ArtistSerializer01.Field.seq(False)
        name = ArtistSerializer01.Field.name(False)
        sch_start_create_dt = ArtistSerializer01.Field.sch_start_create_dt(False)
        sch_end_create_dt = ArtistSerializer01.Field.sch_end_create_dt(False)

        page = PagingFieldSerializer.page(False)
        page_size = PagingFieldSerializer.page_size(False)

        ordering = ArtistSerializer01.Field.ordering(False)

        class Meta:
            ref_name = __qualname__

    class GetResponse(PagingResponseSerializer):
        artists = serializers.ListField(
            child=ArtistSerializer01.List(),
            required=False,
            help_text="아티스트 목록"
        )

        class Meta:
            ref_name = __qualname__

    class DetailGetResponse(ResponseSerializer):
        class DetailGetResponseData(serializers.Serializer):
            artist = ArtistSerializer01.Detail(help_text="아티스트")

            class Meta:
                ref_name = __qualname__

        data = DetailGetResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__
