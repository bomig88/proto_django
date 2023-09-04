from django.contrib import admin

from content.models.album import Album
from content.models.album_detail import AlbumDetail
from content.models.artist import Artist
from content.models.artist_detail import ArtistDetail
from content.models.music import Music
from content.models.music_detail import MusicDetail

admin.site.register(Album)
admin.site.register(AlbumDetail)
admin.site.register(Artist)
admin.site.register(ArtistDetail)
admin.site.register(Music)
admin.site.register(MusicDetail)
