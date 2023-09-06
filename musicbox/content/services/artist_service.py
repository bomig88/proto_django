
from content.filters.artist_filter import ArtistFilter
from content.models.artist import Artist
from content.serializers.artist_serializer import ArtistSerializer, ArtistListSerializer, ArtistDetailSerializer
from core.base.base_service import BaseService


class ArtistService(BaseService):
    queryset_list = Artist.objects.all()
    queryset_detail = Artist.objects.select_related('artist_detail').all()
    serializer = ArtistSerializer
    serializer_list = ArtistListSerializer
    serializer_detail = ArtistDetailSerializer
    filter_set_class = ArtistFilter

