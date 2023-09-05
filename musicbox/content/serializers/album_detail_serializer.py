from rest_framework import serializers

from content.models.album_detail import AlbumDetail


class AlbumDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlbumDetail
        fields = '__all__'
