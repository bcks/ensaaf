# Generated by Django 2.2.10 on 2021-07-04 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0007_auto_20210704_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='profile_id',
            field=models.CharField(blank=True, max_length=10, verbose_name='data.ensaaf.org Profile ID'),
        ),
    ]