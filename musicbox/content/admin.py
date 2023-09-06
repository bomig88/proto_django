from django.contrib import admin

from content.models.album import Album
from content.models.album_additional_info import AlbumAdditionalInfo
from content.models.artist import Artist
from content.models.artist_additional_info import ArtistAdditionalInfo
from content.models.music import Music
from content.models.music_additional_info import MusicAdditionalInfo

admin.site.register(Album)
admin.site.register(AlbumAdditionalInfo)
admin.site.register(Artist)
admin.site.register(ArtistAdditionalInfo)
admin.site.register(Music)
admin.site.register(MusicAdditionalInfo)
