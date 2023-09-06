from rest_framework import serializers

from content.models.artist_additional_info import ArtistAdditionalInfo


class ArtistAdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistAdditionalInfo
        fields = '__all__'


class ArtistAdditionalInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistAdditionalInfo
        fields = '__all__'


class ArtistAdditionalInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistAdditionalInfo
        fields = '__all__'
