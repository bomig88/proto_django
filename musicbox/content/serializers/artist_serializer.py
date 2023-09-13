from rest_framework import serializers

from content.models.artist import Artist
from content.serializers.artist_additional_info_serializer import ArtistAdditionalInfoSerializer


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'


class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class ArtistDetailSerializer(serializers.ModelSerializer):
    artist_additional_info = ArtistAdditionalInfoSerializer(
        many=False,
        source=Artist.artist_additional_info_seq.field.name
    )

    class Meta:
        model = Artist
        fields = '__all__'
