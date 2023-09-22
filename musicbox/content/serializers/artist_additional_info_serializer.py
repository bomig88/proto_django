from rest_framework import serializers

from content.models.artist_additional_info import ArtistAdditionalInfo


class ArtistAdditionalInfoSerializer(serializers.ModelSerializer):
    """
    아티스트 추가 정보 Serializer
    """
    class Meta:
        model = ArtistAdditionalInfo
        fields = '__all__'


class ArtistAdditionalInfoListSerializer(serializers.ModelSerializer):
    """
    아티스트 추가 정보 목록 Serializer
    """
    class Meta:
        model = ArtistAdditionalInfo
        fields = '__all__'


class ArtistAdditionalInfoDetailSerializer(serializers.ModelSerializer):
    """
    아티스트 추가 정보 상세 Serializer
    """
    class Meta:
        model = ArtistAdditionalInfo
        fields = '__all__'
