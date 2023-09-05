from dependency_injector import containers, providers

from content.services.album_detail_service import AlbumDetailService
from content.services.album_service import AlbumService
from content.services.artist_detail_service import ArtistDetailService
from content.services.artist_service import ArtistService
from content.services.music_detail_service import MusicDetailService
from content.services.music_service import MusicService
from content.services.test_services import ContentTestService
from member.services.test_services import MemberTestService


class Services(containers.DeclarativeContainer):
    content_test_service = providers.Singleton(ContentTestService)
    album_service = providers.Singleton(AlbumService)
    album_detail_service = providers.Singleton(AlbumDetailService)
    artist_service = providers.Singleton(ArtistService)
    artist_detail_service = providers.Singleton(ArtistDetailService)
    music_service = providers.Singleton(MusicService)
    music_detail_service = providers.Singleton(MusicDetailService)

    member_test_service = providers.Singleton(MemberTestService)
