# Generated by Django 2.1.3 on 2018-11-21 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_galery', '0003_remove_album_producer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='composer',
        ),
    ]