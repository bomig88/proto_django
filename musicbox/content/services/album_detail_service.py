from content.filters.album_detail_filter import AlbumDetailFilter
from content.models.album_detail import AlbumDetail
from content.serializers.album_detail_serializer import AlbumDetailSerializer
from core.base.base_service import BaseService


class AlbumDetailService(BaseService):
    queryset_list = AlbumDetail.objects.all()
    queryset_detail = AlbumDetail.objects.all()
    serializer = AlbumDetailSerializer
    filter_set_class = AlbumDetailFilter


