from django.db import models


class MusicAdditionalInfo(models.Model):
    """
    곡 추가 정보 모델
    """
    objects = None

    seq = models.BigAutoField(
        primary_key=True,
        help_text='일련번호(PK)'
    )

    lyrics = models.TextField(
        null=True,
        help_text='가사'
    )

    composer = models.CharField(
        null=True,
        max_length=100,
        help_text='작곡가'
    )

    lyricist = models.CharField(
        null=True,
        max_length=100,
        help_text='작사가'
    )

    original_artist = models.CharField(
        null=True,
        max_length=100,
        help_text='원곡자'
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
        db_table = 't_ct_music_additional_info'
        ordering = ['-seq']
