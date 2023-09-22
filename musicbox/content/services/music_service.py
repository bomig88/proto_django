from content.filters.music_filter import MusicFilter
from content.models.music import Music
from content.serializers.music_serializer import MusicSerializer, MusicDetailSerializer, MusicListSerializer
from core.base.base_service import BaseService


class MusicService(BaseService):
    """
    곡 서비스
    """
    queryset_list = (Music.objects
                     .select_related(Music.album_seq.field.name)
                     .all())
    queryset_detail = (Music.objects
                       .select_related(Music.album_seq.field.name)
                       .select_related(Music.music_additional_info_seq.field.name)
                       .all())
    serializer = MusicSerializer
    serializer_list = MusicListSerializer
    serializer_detail = MusicDetailSerializer
    filter_set_class = MusicFilter

