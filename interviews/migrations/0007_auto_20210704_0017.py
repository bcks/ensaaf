# Generated by Django 2.2.10 on 2021-07-04 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0006_auto_20210703_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='profile_id',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='video',
            name='vimeo_id',
            field=models.CharField(blank=True, max_length=64, verbose_name='vimeo ID'),
        ),
    ]