from dependency_injector import containers, providers

from content.services.album_detail_service import AlbumAdditionalInfoService
from content.services.album_service import AlbumService
from content.services.artist_detail_service import ArtistAdditionalInfoService
from content.services.artist_service import ArtistService
from content.services.music_detail_service import MusicAdditionalInfoService
from content.services.music_service import MusicService
from content.services.test_services import ContentTestService
from member.services.member_service import MemberService
from member.services.order_product_service import OrderProductService
from member.services.order_service import OrderService
from member.services.test_services import MemberTestService


class Services(containers.DeclarativeContainer):
    content_test_service = providers.Singleton(ContentTestService)
    album_service = providers.Singleton(AlbumService)
    album_additional_info_service = providers.Singleton(AlbumAdditionalInfoService)
    artist_service = providers.Singleton(ArtistService)
    artist_additional_info_service = providers.Singleton(ArtistAdditionalInfoService)
    music_service = providers.Singleton(MusicService)
    music_additional_info_service = providers.Singleton(MusicAdditionalInfoService)

    member_test_service = providers.Singleton(MemberTestService)
    member_service = providers.Singleton(MemberService)
    order_service = providers.Singleton(OrderService)
    order_product_service = providers.Singleton(OrderProductService)
