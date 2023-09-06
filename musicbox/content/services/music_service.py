from content.filters.music_filter import MusicFilter
from content.models.music import Music
from content.serializers.music_serializer import MusicSerializer, MusicDetailSerializer, MusicListSerializer
from core.base.base_service import BaseService


class MusicService(BaseService):
    queryset_list = Music.objects.all()
    queryset_detail = Music.objects.select_related('music_detail').all()
    serializer = MusicSerializer
    serializer_list = MusicListSerializer
    serializer_detail = MusicDetailSerializer
    filter_set_class = MusicFilter

