# Generated by Django 2.2.10 on 2021-06-04 17:26

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('video', '0005_auto_20210602_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clip',
            name='clip_youtube_id',
        ),
        migrations.RemoveField(
            model_name='video',
            name='youtube_id',
        ),
        migrations.AddField(
            model_name='clip',
            name='clip_vimeo_id',
            field=models.CharField(blank=True, help_text='vimeo ID, if uploaded as a separate clip', max_length=200, verbose_name='vimeo ID'),
        ),
        migrations.AddField(
            model_name='clip',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='video',
            name='vimeo_id',
            field=models.CharField(blank=True, max_length=200, verbose_name='vimeo ID'),
        ),
        migrations.AlterField(
            model_name='clip',
            name='video',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='video.Video'),
        ),
    ]