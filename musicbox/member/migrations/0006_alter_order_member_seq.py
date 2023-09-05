# Generated by Django 4.2.4 on 2023-09-05 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_member_is_staff_alter_member_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='member_seq',
            field=models.OneToOneField(db_column='member_seq', db_constraint=False, help_text='회원 일련번호', on_delete=django.db.models.deletion.CASCADE, related_name='member', to='member.member'),
        ),
    ]
