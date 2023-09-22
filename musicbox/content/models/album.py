from django.db import models

from content.models.album_additional_info import AlbumAdditionalInfo
from content.models.artist import Artist


class Album(models.Model):
    """
    앨범 모델
    """
    objects = None

    class GenreChoices(models.TextChoices):
        JPOP = 'JPOP', '재패니즈 팝'
        POP = 'POP', '팝'
        KPOP = 'KPOP', '한국 팝'
        HIPHOP = 'HIPHOP', '힙합'
        JAZZ = 'JAZZ', '재즈'
        CLASSIC = 'CLASSIC', '클래식'
        CCM = 'CCM', '현대 기독교 음악'
        BALLAD = 'BALLAD', '발라드'
        COUNTRY_MUSIC = 'COUNTRY_MUSIC', '컨트리 뮤직'
        FORK = 'FORK', '포크 음악'
        DISCO = 'DISCO', '디스코'
        DIGITAL_MUSIC = 'DIGITAL_MUSIC', '전자 음악'
        ROCK = 'ROCK', '록 음악'
        TROT = 'TROT', '트로트'
        DANCE_MUSIC = 'DANCE_MUSIC', '댄스 음악'
        EDM = 'EDM', '전자 댄스 음악'
        ROCK_N_ROLL = 'ROCK_N_ROLL', '로큰롤'
        BLUES = 'BLUES', '블루스'

    seq = models.BigAutoField(
        primary_key=True,
        help_text='일련번호(PK)'
    )

    name = models.CharField(
        max_length=80,
        help_text='앨범명'
    )

    genre = models.CharField(
        choices=GenreChoices.choices,
        max_length=15,
        help_text='장르'
    )

    artist_seq = models.OneToOneField(
        Artist,
        on_delete=models.CASCADE,
        db_column='artist_seq',
        db_constraint=False,
        null=True,
        help_text='아티스트 일련번호'
    )

    album_additional_info_seq = models.OneToOneField(
        AlbumAdditionalInfo,
        on_delete=models.CASCADE,
        db_column='album_additional_info_seq',
        db_constraint=False,
        null=True,
        help_text='앨범 추가 정보 일련번호'
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
        db_table = 't_ct_album'
        ordering = ['-seq']
