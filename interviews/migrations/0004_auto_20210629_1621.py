# Generated by Django 2.2.10 on 2021-06-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0003_auto_20210629_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='image',
            field=models.ImageField(blank=True, max_length=200, upload_to='themes/'),
        ),
    ]
