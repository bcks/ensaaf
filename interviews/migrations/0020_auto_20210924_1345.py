# Generated by Django 2.2.10 on 2021-09-24 13:45

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0019_auto_20210708_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clip',
            name='transcription',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='transcription',
            field=tinymce.models.HTMLField(blank=True, default=None, null=True),
        ),
    ]
