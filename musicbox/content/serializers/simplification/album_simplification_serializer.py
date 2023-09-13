from rest_framework import serializers

from content.models.album import Album


class AlbumSimplificationSerializer(serializers.ModelSerializer):
    class Default(serializers.ModelSerializer):

        class Meta:
            model = Album
            fields = [
                Album.seq.field.name,
                Album.name.field.name,
                Album.artist_seq.field.name,
                Album.genre.field.name,
                Album.create_at.field.name,
            ]
