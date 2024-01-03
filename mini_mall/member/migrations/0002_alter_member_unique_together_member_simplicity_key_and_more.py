# Generated by Django 4.2.4 on 2023-11-14 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='member',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='member',
            name='simplicity_key',
            field=models.CharField(help_text='간편 인증 값', max_length=3200, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='tag',
            field=models.CharField(choices=[('basic_user', '일반 사용자'), ('simplicity_user', '간편 가입 사용자'), ('manager', '관리자'), ('super_manager', '상위 관리자')], default='basic_user', help_text='분류', max_length=30),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('M', '남성'), ('F', '여성'), ('N', '미설정')], default='N', help_text='성별(M:남, F:여, N:미설정)', max_length=1),
        ),
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.CharField(choices=[('join', '가입'), ('leave', '탈퇴')], default='join', help_text='상태', max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='member',
            unique_together={('username', 'email', 'tag')},
        ),
        migrations.RemoveField(
            model_name='member',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='member',
            name='is_superuser',
        ),
    ]