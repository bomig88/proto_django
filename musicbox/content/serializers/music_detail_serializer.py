from rest_framework import serializers

from content.models.music_detail import MusicDetail


class MusicDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = MusicDetail
        fields = '__all__'
