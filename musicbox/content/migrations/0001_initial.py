# Generated by Django 4.2.4 on 2023-09-22 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('seq', models.BigAutoField(help_text='일련번호(PK)', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='앨범명', max_length=80)),
                ('genre', models.CharField(choices=[('JPOP', '재패니즈 팝'), ('POP', '팝'), ('KPOP', '한국 팝'), ('HIPHOP', '힙합'), ('JAZZ', '재즈'), ('CLASSIC', '클래식'), ('CCM', '현대 기독교 음악'), ('BALLAD', '발라드'), ('COUNTRY_MUSIC', '컨트리 뮤직'), ('FORK', '포크 음악'), ('DISCO', '디스코'), ('DIGITAL_MUSIC', '전자 음악'), ('ROCK', '록 음악'), ('TROT', '트로트'), ('DANCE_MUSIC', '댄스 음악'), ('EDM', '전자 댄스 음악'), ('ROCK_N_ROLL', '로큰롤'), ('BLUES', '블루스')], help_text='장르', max_length=15)),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='생성일시')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='수정일시')),
            ],
            options={
                'db_table': 't_ct_album',
                'ordering': ['-seq'],
            },
        ),
        migrations.CreateModel(
            name='AlbumAdditionalInfo',
            fields=[
                ('seq', models.BigAutoField(help_text='일련번호(PK)', primary_key=True, serialize=False)),
                ('description', models.TextField(help_text='앨범 상세 설명', null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='생성일시')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='수정일시')),
            ],
            options={
                'db_table': 't_ct_album_additional_info',
                'ordering': ['-seq'],
            },
        ),
        migrations.CreateModel(
            name='ArtistAdditionalInfo',
            fields=[
                ('seq', models.BigAutoField(help_text='일련번호(PK)', primary_key=True, serialize=False)),
                ('description', models.TextField(help_text='아티스트 상세 설명', null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='생성일시')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='수정일시')),
            ],
            options={
                'db_table': 't_ct_artist_additional_info',
                'ordering': ['-seq'],
            },
        ),
        migrations.CreateModel(
            name='MusicAdditionalInfo',
            fields=[
                ('seq', models.BigAutoField(help_text='일련번호(PK)', primary_key=True, serialize=False)),
                ('lyrics', models.TextField(help_text='가사', null=True)),
                ('composer', models.CharField(help_text='작곡가', max_length=100, null=True)),
                ('lyricist', models.CharField(help_text='작사가', max_length=100, null=True)),
                ('original_artist', models.CharField(help_text='원곡자', max_length=100, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='생성일시')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='수정일시')),
            ],
            options={
                'db_table': 't_ct_music_additional_info',
                'ordering': ['-seq'],
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('seq', models.BigAutoField(help_text='일련번호(PK)', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='곡 명', max_length=80)),
                ('play_time', models.IntegerField(default=0, help_text='재생시간(초)')),
                ('price', models.IntegerField(default=0, help_text='판매가')),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='생성일시')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='수정일시')),
                ('album_seq', models.ForeignKey(db_column='album_seq', db_constraint=False, help_text='앨범 코드', null=True, on_delete=django.db.models.deletion.CASCADE, to='content.album')),
                ('music_additional_info_seq', models.OneToOneField(db_column='music_additional_info_seq', db_constraint=False, help_text='곡 추가 정보 일련번호', null=True, on_delete=django.db.models.deletion.CASCADE, to='content.musicadditionalinfo')),
            ],
            options={
                'db_table': 't_ct_music',
                'ordering': ['-seq'],
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('seq', models.BigAutoField(help_text='일련번호(PK)', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='아티스트 명', max_length=80)),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='생성일시')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='수정일시')),
                ('artist_additional_info_seq', models.OneToOneField(db_column='artist_additional_info_seq', db_constraint=False, help_text='아티스트 추가 정보 일련번호', null=True, on_delete=django.db.models.deletion.CASCADE, to='content.artistadditionalinfo')),
            ],
            options={
                'db_table': 't_ct_artist',
                'ordering': ['-seq'],
            },
        ),
        migrations.AddField(
            model_name='album',
            name='album_additional_info_seq',
            field=models.OneToOneField(db_column='album_additional_info_seq', db_constraint=False, help_text='앨범 추가 정보 일련번호', null=True, on_delete=django.db.models.deletion.CASCADE, to='content.albumadditionalinfo'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist_seq',
            field=models.OneToOneField(db_column='artist_seq', db_constraint=False, help_text='아티스트 일련번호', null=True, on_delete=django.db.models.deletion.CASCADE, to='content.artist'),
        ),
    ]
