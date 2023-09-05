
from content.filters.artist_filter import ArtistFilter
from content.models.artist import Artist
from content.serializers.artist_serializer import ArtistSerializer
from core.base.base_service import BaseService


class ArtistService(BaseService):
    queryset_list = Artist.objects.all()
    queryset_detail = Artist.objects.select_related('artist_detail').all()
    serializer = ArtistSerializer
    filter_set_class = ArtistFilter

