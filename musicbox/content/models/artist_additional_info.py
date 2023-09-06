from django.db import models

from content.models.artist import Artist


class ArtistAdditionalInfo(models.Model):
    objects = None

    seq = models.BigAutoField(
        primary_key=True,
        help_text='일련번호(PK)'
    )

    artist_seq = models.OneToOneField(
        Artist,
        on_delete=models.CASCADE,
        db_column='artist_seq',
        db_constraint=False,
        related_name='artist_detail',
        help_text='아티스트 일련번호'
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
        db_table = 't_ct_artist_additional_info'
        ordering = ['-seq']
