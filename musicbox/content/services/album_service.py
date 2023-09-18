from content.filters.album_filter import AlbumFilter
from content.models.album import Album
from content.models.music import Music
from content.serializers.album_serializer import AlbumSerializer, AlbumDetailSerializer, AlbumListSerializer
from core.base.base_service import BaseService


class AlbumService(BaseService):
    """
    앨범 서비스
    """
    queryset_list = (Album.objects
                     .select_related(Album.artist_seq.field.name)
                     .all())
    queryset_detail = (Album.objects.select_related(Album.artist_seq.field.name)
                       .select_related(Album.album_additional_info_seq.field.name)
                       .prefetch_related(f'{Music.__name__.lower()}_set')
                       .all())
    serializer = AlbumSerializer
    serializer_list = AlbumListSerializer
    serializer_detail = AlbumDetailSerializer
    filter_set_class = AlbumFilter


