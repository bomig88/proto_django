from dependency_injector import containers, providers

from content.services.album_additional_info_service import AlbumAdditionalInfoService
from content.services.album_service import AlbumService
from content.services.artist_additional_info_service import ArtistAdditionalInfoService
from content.services.artist_service import ArtistService
from content.services.music_additional_info_service import MusicAdditionalInfoService
from content.services.music_service import MusicService
from member.services.member_service import MemberService
from order.services.order_product_service import OrderProductService
from order.services.order_service import OrderService


class Services(containers.DeclarativeContainer):
    # content
    album_service = providers.Singleton(AlbumService)
    album_additional_info_service = providers.Singleton(AlbumAdditionalInfoService)
    artist_service = providers.Singleton(ArtistService)
    artist_additional_info_service = providers.Singleton(ArtistAdditionalInfoService)
    music_service = providers.Singleton(MusicService)
    music_additional_info_service = providers.Singleton(MusicAdditionalInfoService)

    # member
    member_service = providers.Singleton(MemberService)

    # order
    order_service = providers.Singleton(OrderService)
    order_product_service = providers.Singleton(OrderProductService)
