from rest_framework import serializers

from content.filters.music_filter import MusicFilter
from content.models.music import Music
from content.views.serializers.music_additional_info_serializer import MusicAdditionalInfoSerializer01
from content.views.serializers.simplification.album_simplification_serializer import AlbumSimplificationSerializer01
from core.base.swagger_response_serializer import ResponseSerializer


class MusicSerializer01:
    """
    Swagger 곡 Serializer
    """
    class Default(serializers.ModelSerializer):

        class Meta:
            model = Music
            fields = '__all__'
            ref_name = __qualname__

    class List(serializers.ModelSerializer):
        album = AlbumSimplificationSerializer01.Default(many=False, read_only=True)

        class Meta:
            model = Music
            fields = '__all__'
            ref_name = __qualname__

    class Detail(serializers.ModelSerializer):
        album = AlbumSimplificationSerializer01.Default(many=False, read_only=True)
        music_additional_info = MusicAdditionalInfoSerializer01.Detail(many=False)

        class Meta:
            model = Music
            fields = '__all__'
            ref_name = __qualname__

    class Field(serializers.Serializer):
        @staticmethod
        def seq(required=True):
            seq = serializers.IntegerField(
                required=required,
                help_text=Music.seq.field.help_text
            )
            return seq

        @staticmethod
        def album_seq(required=True):
            album_seq = serializers.IntegerField(
                required=required,
                help_text=Music.album_seq.field.help_text
            )
            return album_seq

        @staticmethod
        def name(required=True):
            name = serializers.CharField(
                required=required,
                help_text=Music.name.field.help_text
            )
            return name

        @staticmethod
        def sch_start_create_dt(required=True):
            sch_start_create_dt = serializers.DateTimeField(
                required=required,
                help_text=MusicFilter.base_filters['sch_start_create_dt'].field.help_text
            )
            return sch_start_create_dt

        @staticmethod
        def sch_end_create_dt(required=True):
            sch_end_create_dt = serializers.DateTimeField(
                required=required,
                help_text=MusicFilter.base_filters['sch_end_create_dt'].field.help_text
            )
            return sch_end_create_dt

        @staticmethod
        def ordering(required=False):
            ordering = serializers.ChoiceField(
                choices=list(MusicFilter.base_filters['ordering'].param_map.values()),
                required=required,
                help_text=MusicFilter.base_filters['ordering'].field.help_text
            )
            return ordering


class MusicSerializer02:
    """
    Swagger 곡 Serializer
    """
    class GetParam(serializers.Serializer):
        seq = MusicSerializer01.Field.seq(False)
        album_seq = MusicSerializer01.Field.album_seq(False)
        name = MusicSerializer01.Field.name(False)
        sch_start_create_dt = MusicSerializer01.Field.sch_start_create_dt(False)
        sch_end_create_dt = MusicSerializer01.Field.sch_end_create_dt(False)
        ordering = MusicSerializer01.Field.ordering(False)

        class Meta:
            ref_name = __qualname__

    class GetResponse(serializers.Serializer):
        musics = serializers.ListField(
            child=MusicSerializer01.List(),
            required=False,
            help_text="곡 목록"
        )

        class Meta:
            ref_name = __qualname__

    class DetailGetResponse(ResponseSerializer):
        class DetailGetResponseData(serializers.Serializer):
            music = MusicSerializer01.Detail(help_text="곡")

            class Meta:
                ref_name = __qualname__

        data = DetailGetResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__
