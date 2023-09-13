from rest_framework import serializers

from content.models.album import Album
from content.models.music import Music


class MusicSimplificationSerializer(serializers.ModelSerializer):
    class Default(serializers.ModelSerializer):

        class Meta:
            model = Music
            fields = [
                Music.seq.field.name,
                Music.name.field.name,
                Music.album_seq.field.name,
                Music.price.field.name,
                Music.create_at.field.name,
            ]
