from django.db import models

from content.models.artist_additional_info import ArtistAdditionalInfo


class Artist(models.Model):
    """
    아티스트 모델
    """
    objects = None

    seq = models.BigAutoField(
        primary_key=True,
        help_text='일련번호(PK)'
    )

    artist_additional_info_seq = models.OneToOneField(
        ArtistAdditionalInfo,
        on_delete=models.CASCADE,
        db_column='artist_additional_info_seq',
        db_constraint=False,
        null=True,
        help_text='아티스트 추가 정보 일련번호'
    )

    name = models.CharField(
        max_length=80,
        help_text='아티스트 명'
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
        db_table = 't_ct_artist'
        ordering = ['-seq']
