from content.filters.artist_additional_info_filter import ArtistAdditionalInfoFilter
from content.models.artist_additional_info import ArtistAdditionalInfo
from content.serializers.artist_additional_info_serializer import ArtistAdditionalInfoSerializer, \
    ArtistAdditionalInfoListSerializer, ArtistAdditionalInfoDetailSerializer
from core.base.base_service import BaseService


class ArtistAdditionalInfoService(BaseService):
    queryset_list = ArtistAdditionalInfo.objects.all()
    queryset_detail = ArtistAdditionalInfo.objects.all()
    serializer = ArtistAdditionalInfoSerializer
    serializer_list = ArtistAdditionalInfoListSerializer
    serializer_detail = ArtistAdditionalInfoDetailSerializer
    filter_set_class = ArtistAdditionalInfoFilter
