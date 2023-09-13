from rest_framework import serializers

from content.filters.album_filter import AlbumFilter
from content.models.album import Album
from content.views.serializers.album_additional_info_serializer import AlbumAdditionalInfoSerializer01
from content.views.serializers.artist_serializer import ArtistSerializer01
from content.views.serializers.simplification.music_simplification_serializer import MusicSimplificationSerializer01
from core.base.swagger_response_serializer import ResponseSerializer


class AlbumSerializer01:
    class Default(serializers.ModelSerializer):

        class Meta:
            model = Album
            fields = '__all__'
            ref_name = __qualname__

    class List(serializers.ModelSerializer):
        artist = ArtistSerializer01.Default(many=False, read_only=True)

        class Meta:
            model = Album
            fields = '__all__'
            ref_name = __qualname__

    class Detail(serializers.ModelSerializer):
        album_additional_info = AlbumAdditionalInfoSerializer01.Detail(many=False)
        artist = ArtistSerializer01.Default(many=False, read_only=True)
        musics = MusicSimplificationSerializer01.Default(many=True)

        class Meta:
            model = Album
            fields = '__all__'
            ref_name = __qualname__

    class Field(serializers.Serializer):
        @staticmethod
        def seq(required=True):
            seq = serializers.IntegerField(
                required=required,
                help_text=Album.seq.field.help_text
            )
            return seq

        @staticmethod
        def name(required=True):
            name = serializers.CharField(
                required=required,
                help_text=Album.name.field.help_text
            )
            return name

        @staticmethod
        def genre(required=True):
            genre = serializers.ChoiceField(
                choices=tuple(Album.GenreChoices.choices),
                required=required,
                help_text=f'{Album.genre.field.help_text} \ {str(Album.GenreChoices.choices)}'
            )
            return genre

        @staticmethod
        def sch_start_create_dt(required=True):
            sch_start_create_dt = serializers.DateTimeField(
                required=required,
                help_text=AlbumFilter.base_filters['sch_start_create_dt'].field.help_text
            )
            return sch_start_create_dt

        @staticmethod
        def sch_end_create_dt(required=True):
            sch_end_create_dt = serializers.DateTimeField(
                required=required,
                help_text=AlbumFilter.base_filters['sch_end_create_dt'].field.help_text
            )
            return sch_end_create_dt

        @staticmethod
        def ordering(required=False):
            ordering = serializers.ChoiceField(
                choices=list(AlbumFilter.base_filters['ordering'].param_map.values()),
                required=required,
                help_text=AlbumFilter.base_filters['ordering'].field.help_text
            )
            return ordering


class AlbumSerializer02:
    class GetParam(serializers.Serializer):
        seq = AlbumSerializer01.Field.seq(False)
        name = AlbumSerializer01.Field.name(False)
        sch_start_create_dt = AlbumSerializer01.Field.sch_start_create_dt(False)
        sch_end_create_dt = AlbumSerializer01.Field.sch_end_create_dt(False)
        ordering = AlbumSerializer01.Field.ordering(False)

        class Meta:
            ref_name = __qualname__

    class GetResponse(serializers.Serializer):
        albums = serializers.ListField(
            child=AlbumSerializer01.List(),
            required=False,
            help_text="앨범 목록"
        )

        class Meta:
            ref_name = __qualname__

    class DetailGetResponse(ResponseSerializer):
        class DetailGetResponseData(serializers.Serializer):
            album = AlbumSerializer01.Detail(help_text="앨범")

            class Meta:
                ref_name = __qualname__

        data = DetailGetResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__
