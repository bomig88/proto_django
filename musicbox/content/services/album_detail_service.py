from content.filters.album_additional_info_filter import AlbumAdditionalInfoFilter
from content.models.album_additional_info import AlbumAdditionalInfo
from content.serializers.album_additional_info_serializer import AlbumAdditionalInfoSerializer, \
    AlbumAdditionalInfoListSerializer, AlbumAdditionalInfoDetailSerializer
from core.base.base_service import BaseService


class AlbumAdditionalInfoService(BaseService):
    queryset_list = AlbumAdditionalInfo.objects.all()
    queryset_detail = AlbumAdditionalInfo.objects.all()
    serializer = AlbumAdditionalInfoSerializer
    serializer_list = AlbumAdditionalInfoListSerializer
    serializer_detail = AlbumAdditionalInfoDetailSerializer
    filter_set_class = AlbumAdditionalInfoFilter


