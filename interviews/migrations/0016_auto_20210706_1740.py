# Generated by Django 2.2.10 on 2021-07-06 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0015_auto_20210706_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='village',
            field=models.CharField(blank=True, max_length=10, verbose_name='Village Census Code'),
        ),
    ]