from django.contrib import admin

from content.models.album import Album
from content.models.album_additional_info import AlbumAdditionalInfo
from content.models.artist import Artist
from content.models.artist_additional_info import ArtistAdditionalInfo
from content.models.music import Music
from content.models.music_additional_info import MusicAdditionalInfo


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('seq', 'name', 'genre', 'artist_name', 'album_additional_info_seq', 'create_at')
    list_select_related = ['artist_seq']  # To avoid extra queries

    def artist_name(self, album):
        return album.artist_seq.name  # Foreign key relationship


@admin.register(AlbumAdditionalInfo)
class AlbumAdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ('seq', 'create_at')


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('seq', 'name', 'artist_additional_info_seq', 'create_at')


@admin.register(ArtistAdditionalInfo)
class ArtistAdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ('seq', 'create_at')


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('seq', 'name', 'play_time', 'price', 'album_name', 'music_additional_info_seq', 'create_at')
    list_select_related = ['album_seq']  # To avoid extra queries

    def album_name(self, music):
        return music.album_seq.name  # Foreign key relationship


@admin.register(MusicAdditionalInfo)
class MusicAdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ('seq', 'create_at')
