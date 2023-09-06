from rest_framework import serializers

from content.models.music import Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


class MusicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
