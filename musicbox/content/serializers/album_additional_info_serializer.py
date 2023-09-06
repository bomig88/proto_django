from rest_framework import serializers

from content.models.album_additional_info import AlbumAdditionalInfo


class AlbumAdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumAdditionalInfo
        fields = '__all__'


class AlbumAdditionalInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumAdditionalInfo
        fields = '__all__'


class AlbumAdditionalInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumAdditionalInfo
        fields = '__all__'
