from rest_framework import serializers

from content.models.album import Album
from content.models.music import Music
from content.serializers.album_additional_info_serializer import AlbumAdditionalInfoSerializer
from content.serializers.artist_serializer import ArtistSerializer
from content.serializers.simplification.music_simplification_serializer import MusicSimplificationSerializer


class AlbumSerializer(serializers.ModelSerializer):
    """
    앨범 Serializer
    """
    class Meta:
        model = Album
        fields = '__all__'


class AlbumListSerializer(serializers.ModelSerializer):
    """
    앨범 목록 Serializer
    """
    artist = ArtistSerializer(
        many=False,
        read_only=True,
        source=Album.artist_seq.field.name
    )

    class Meta:
        model = Album
        fields = '__all__'


class AlbumDetailSerializer(serializers.ModelSerializer):
    """
    앨범 상세 Serializer
    """
    album_additional_info = AlbumAdditionalInfoSerializer(
        many=False,
        source=Album.album_additional_info_seq.field.name
    )

    artist = ArtistSerializer(
        many=False,
        read_only=True,
        source=Album.artist_seq.field.name
    )

    musics = MusicSimplificationSerializer(
        many=True,
        required=False,
        source=f'{Music.__name__.lower()}_set'
    )

    class Meta:
        model = Album
        fields = '__all__'
