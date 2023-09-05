from rest_framework import serializers

from content.models.artist_detail import ArtistDetail


class ArtistDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArtistDetail
        fields = '__all__'
