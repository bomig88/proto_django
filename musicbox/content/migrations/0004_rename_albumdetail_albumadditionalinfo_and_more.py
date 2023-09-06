# Generated by Django 4.2.4 on 2023-09-06 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_remove_album_artist_code_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AlbumDetail',
            new_name='AlbumAdditionalInfo',
        ),
        migrations.RenameModel(
            old_name='ArtistDetail',
            new_name='ArtistAdditionalInfo',
        ),
        migrations.RenameModel(
            old_name='MusicDetail',
            new_name='MusicAdditionalInfo',
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('JPOP', '재패니즈 팝'), ('POP', '팝'), ('KPOP', '한국 팝'), ('HIPHOP', '힙합'), ('JAZZ', '재즈'), ('CLASSIC', '클래식'), ('CCM', '현대 기독교 음악'), ('BALLAD', '발라드'), ('COUNTRY_MUSIC', '컨트리 뮤직'), ('FORK', '포크 음악'), ('DISCO', '디스코'), ('DIGITAL_MUSIC', '전자 음악'), ('ROCK', '록 음악'), ('TROT', '트로트'), ('DANCE_MUSIC', '댄스 음악'), ('EDM', '전자 댄스 음악'), ('ROCK_N_ROLL', '로큰롤'), ('BLUES', '블루스')], help_text='장르', max_length=15),
        ),
        migrations.AlterField(
            model_name='music',
            name='play_time',
            field=models.IntegerField(default=0, help_text='재생시간(초)'),
        ),
        migrations.AlterModelTable(
            name='albumadditionalinfo',
            table='t_ct_album_additional_info',
        ),
        migrations.AlterModelTable(
            name='artistadditionalinfo',
            table='t_ct_artist_additional_info',
        ),
        migrations.AlterModelTable(
            name='musicadditionalinfo',
            table='t_ct_music_additional_info',
        ),
    ]