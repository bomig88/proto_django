from rest_framework import serializers

from content.models.music import Music
from content.serializers.music_additional_info_serializer import MusicAdditionalInfoSerializer
from content.serializers.simplification.album_simplification_serializer import AlbumSimplificationSerializer


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


class MusicListSerializer(serializers.ModelSerializer):
    album = AlbumSimplificationSerializer.Default(
        many=False,
        read_only=True,
        source=Music.album_seq.field.name
    )

    class Meta:
        model = Music
        fields = '__all__'


class MusicDetailSerializer(serializers.ModelSerializer):
    album = AlbumSimplificationSerializer.Default(
        many=False,
        read_only=True,
        source=Music.album_seq.field.name
    )

    music_additional_info = MusicAdditionalInfoSerializer(
        many=False,
        source=Music.music_additional_info_seq.field.name
    )

    class Meta:
        model = Music
        fields = '__all__'
