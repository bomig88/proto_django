from content.filters.music_additional_info_filter import MusicAdditionalInfoFilter
from content.models.music_additional_info import MusicAdditionalInfo
from content.serializers.music_additional_info_serializer import MusicAdditionalInfoSerializer, \
    MusicAdditionalInfoListSerializer, MusicAdditionalInfoDetailSerializer
from core.base.base_service import BaseService


class MusicAdditionalInfoService(BaseService):
    queryset_list = MusicAdditionalInfo.objects.all()
    queryset_detail = MusicAdditionalInfo.objects.all()
    serializer = MusicAdditionalInfoSerializer
    serializer_list = MusicAdditionalInfoListSerializer
    serializer_detail = MusicAdditionalInfoDetailSerializer
    filter_set_class = MusicAdditionalInfoFilter


