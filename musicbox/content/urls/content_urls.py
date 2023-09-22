from django.urls import path


from content.views.album_views import AlbumView, AlbumDetailView
from content.views.artist_views import ArtistView, ArtistDetailView
from content.views.music_views import MusicView, MusicDetailView

urlpatterns = [
    path('/albums', AlbumView.as_view()),
    path('/albums/<int:seq>', AlbumDetailView.as_view()),

    path('/artists', ArtistView.as_view()),
    path('/artists/<int:seq>', ArtistDetailView.as_view()),

    path('/musics', MusicView.as_view()),
    path('/musics/<int:seq>', MusicDetailView.as_view()),
]
