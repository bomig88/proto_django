from django.db import models


class AlbumAdditionalInfo(models.Model):
    """
    앨범 추가 정보 모델
    """
    objects = None

    seq = models.BigAutoField(
        primary_key=True,
        help_text='일련번호(PK)'
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
        db_table = 't_ct_album_additional_info'
        ordering = ['-seq']
