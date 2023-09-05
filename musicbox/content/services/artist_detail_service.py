from content.filters.artist_detail_filter import ArtistDetailFilter
from content.models.artist_detail import ArtistDetail
from content.serializers.artist_detail_serializer import ArtistDetailSerializer
from core.base.base_service import BaseService


class ArtistDetailService(BaseService):
    queryset_list = ArtistDetail.objects.all()
    queryset_detail = ArtistDetail.objects.all()
    serializer = ArtistDetailSerializer
    filter_set_class = ArtistDetailFilter


