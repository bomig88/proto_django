from content.filters.music_detail_filter import MusicDetailFilter
from content.models.music_detail import MusicDetail
from content.serializers.music_detail_serializer import MusicDetailSerializer
from core.base.base_service import BaseService


class MusicDetailService(BaseService):
    queryset_list = MusicDetail.objects.all()
    queryset_detail = MusicDetail.objects.all()
    serializer = MusicDetailSerializer
    filter_set_class = MusicDetailFilter


