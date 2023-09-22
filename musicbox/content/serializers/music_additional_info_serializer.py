from rest_framework import serializers

from content.models.music_additional_info import MusicAdditionalInfo


class MusicAdditionalInfoSerializer(serializers.ModelSerializer):
    """
    곡 추가 정보 Serializer
    """
    class Meta:
        model = MusicAdditionalInfo
        fields = '__all__'


class MusicAdditionalInfoListSerializer(serializers.ModelSerializer):
    """
    곡 추가 정보 목록 Serializer
    """
    class Meta:
        model = MusicAdditionalInfo
        fields = '__all__'


class MusicAdditionalInfoDetailSerializer(serializers.ModelSerializer):
    """
    곡 추가 정보 상세 Serializer
    """
    class Meta:
        model = MusicAdditionalInfo
        fields = '__all__'
