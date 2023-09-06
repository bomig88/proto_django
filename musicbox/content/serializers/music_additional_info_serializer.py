from rest_framework import serializers

from content.models.music_additional_info import MusicAdditionalInfo


class MusicAdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicAdditionalInfo
        fields = '__all__'


class MusicAdditionalInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicAdditionalInfo
        fields = '__all__'


class MusicAdditionalInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicAdditionalInfo
        fields = '__all__'
