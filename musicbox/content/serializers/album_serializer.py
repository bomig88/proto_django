from rest_framework import serializers

from content.models.album import Album
from content.models.artist import Artist
from content.models.music import Music
from content.serializers.artist_serializer import ArtistSerializer
from content.serializers.music_serializer import MusicSerializer


class AlbumSerializer(serializers.ModelSerializer):
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
