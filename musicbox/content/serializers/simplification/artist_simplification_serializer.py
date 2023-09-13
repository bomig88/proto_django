from rest_framework import serializers

from content.models.album import Album
from content.models.artist import Artist


class ArtistSimplificationSerializer(serializers.ModelSerializer):
    class Default(serializers.ModelSerializer):

        class Meta:
            model = Artist
            fields = [
                Artist.seq.field.name,
                Artist.name.field.name,
                Artist.create_at.field.name,
            ]