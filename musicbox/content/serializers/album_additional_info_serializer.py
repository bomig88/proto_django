from rest_framework import serializers

from content.models.album_additional_info import AlbumAdditionalInfo


class AlbumAdditionalInfoSerializer(serializers.ModelSerializer):
    """
    앨범 추가 정보 Serializer
    """
    class Meta:
        model = AlbumAdditionalInfo
        fields = '__all__'


class AlbumAdditionalInfoListSerializer(serializers.ModelSerializer):
    """
    앨범 추가 정보 목록 Serializer
    """
    class Meta:
        model = AlbumAdditionalInfo
        fields = '__all__'


class AlbumAdditionalInfoDetailSerializer(serializers.ModelSerializer):
    """
    앨범 추가 정보 상세 Serializer
    """
    class Meta:
        model = AlbumAdditionalInfo
        fields = '__all__'
