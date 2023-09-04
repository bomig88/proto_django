from django.db import models

from content.models.album import Album


class AlbumDetail(models.Model):
    object = None

    seq = models.BigAutoField(
        primary_key=True,
        help_text='일련번호(PK)'
    )

    album_code = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        db_column='album_code',
        db_constraint=False,
        help_text='앨범 코드'
    )

    description = models.TextField(
        null=True,
        help_text='앨범 상세 설명'
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
        db_table = 't_ct_album_detail'
        ordering = ['-seq']
