from content.filters.artist_additional_info_filter import ArtistAdditionalInfoFilter
from content.models.artist_additional_info import ArtistAdditionalInfo
from content.serializers.artist_additional_info_serializer import ArtistAdditionalInfoSerializer, \
    ArtistAdditionalInfoListSerializer, ArtistAdditionalInfoDetailSerializer
from core.base.base_service import BaseService


class ArtistAdditionalInfoService(BaseService):
    """
    아티스트 추가 정보 서비스
    """
    queryset_list = ArtistAdditionalInfo.objects.all()
    queryset_detail = ArtistAdditionalInfo.objects.all()
    serializer = ArtistAdditionalInfoSerializer
    serializer_list = ArtistAdditionalInfoListSerializer
    serializer_detail = ArtistAdditionalInfoDetailSerializer
    filter_set_class = ArtistAdditionalInfoFilter
