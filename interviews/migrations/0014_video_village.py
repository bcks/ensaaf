# Generated by Django 2.2.10 on 2021-07-06 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0013_villages'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='village',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, to='interviews.Villages'),
        ),
    ]