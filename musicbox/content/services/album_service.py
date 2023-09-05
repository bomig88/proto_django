from content.filters.album_filter import AlbumFilter
from content.models.album import Album
from content.models.music import Music
from content.serializers.album_serializer import AlbumSerializer
from core.base.base_service import BaseService


class AlbumService(BaseService):
    queryset_list = Album.objects.select_related('artist_seq').prefetch_related(f'{Music.__name__.lower()}_set').all()
    queryset_detail = Album.objects.select_related('album_detail').all()
    serializer = AlbumSerializer
    filter_set_class = AlbumFilter


