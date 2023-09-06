from rest_framework import serializers

from content.models.album import Album
from content.models.album_additional_info import AlbumAdditionalInfo
from content.models.music import Music
from content.serializers.album_additional_info_serializer import AlbumAdditionalInfoDetailSerializer
from content.serializers.artist_serializer import ArtistSerializer
from content.serializers.music_serializer import MusicSerializer


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class AlbumListSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(
        many=False,
        read_only=True,
        source=Album.artist_seq.field.name
    )

    musics = MusicSerializer(
        many=True,
        required=False,
        source=f'{Music.__name__.lower()}_set'
    )

    class Meta:
        model = Album
        fields = '__all__'


class AlbumDetailSerializer(serializers.ModelSerializer):
    album_detail = AlbumAdditionalInfoDetailSerializer(
        many=True,
        required=False,
        source=f'{AlbumAdditionalInfo.__name__.lower()}_set'
    )

    class Meta:
        model = Album
        fields = '__all__'
