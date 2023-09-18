from django.db import models

from content.models.album import Album
from content.models.music_additional_info import MusicAdditionalInfo


class Music(models.Model):
    """
    곡 모델
    """
    objects = None

    seq = models.BigAutoField(
        primary_key=True,
        help_text='일련번호(PK)'
    )

    name = models.CharField(
        max_length=80,
        help_text='곡 명'
    )

    play_time = models.IntegerField(
        default=0,
        help_text='재생시간(초)'
    )

    price = models.IntegerField(
        default=0,
        help_text='판매가'
    )

    album_seq = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        db_column='album_seq',
        db_constraint=False,
        null=True,
        help_text='앨범 코드'
    )

    music_additional_info_seq = models.OneToOneField(
        MusicAdditionalInfo,
        on_delete=models.CASCADE,
        db_column='music_additional_info_seq',
        db_constraint=False,
        null=True,
        help_text='곡 추가 정보 일련번호'
    )

    create_at = models.DateTimeField(
        auto_now_add=True,
        help_text='생성일시'
    )

    update_at = models.DateTimeField(
        auto_now=True,
        help_text='수정일시'
    )

    class Meta:
        db_table = 't_ct_music'
        ordering = ['-seq']
