from django.db import models

from content.models.artist import Artist


class ArtistDetail(models.Model):
    object = None

    seq = models.BigAutoField(
        primary_key=True,
        help_text='일련번호(PK)'
    )

    artist_code = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        db_column='artist_code',
        db_constraint=False,
        help_text='아티스트 코드'
    )

    description = models.TextField(
        null=True,
        help_text='아티스트 상세 설명'
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
        db_table = 't_ct_artist_detail'
        ordering = ['-seq']
