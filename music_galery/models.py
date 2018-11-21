from django.db import models
from django.conf import settings


class Band(models.Model):
    artists = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bands')
    name = models.CharField(max_length=255)
    

class Album(models.Model):
    band = models.ForeignKey(Band, models.CASCADE, related_name='albums')

    title = models.CharField(max_length=255)
    release_date = models.DateField()


class Song(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, models.CASCADE, related_name='songs')
