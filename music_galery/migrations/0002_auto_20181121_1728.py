# Generated by Django 2.1.3 on 2018-11-21 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music_galery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('artists', models.ManyToManyField(related_name='bands', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='artists',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='music_galery.Album'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='music_galery.Band'),
            preserve_default=False,
        ),
    ]
