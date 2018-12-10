from promise import Promise
from promise.dataloader import DataLoader

from django.contrib.auth.models import User
from music_galery.models import Band, Album, Song


def users_query():
    return User.objects.prefetch_related('bands')

def bands_query(): 
    return Band.objects.prefetch_related('artists', 'albums')

def albums_query():
    return Album.objects.select_related('band').prefetch_related('songs')

def songs_query():
    return Song.objects.select_related('album')


def reorder(ordered_ids, items):
    items_dict = {i.id: i for i in items}
    return [items_dict[i] for i in ordered_ids]


def load_users(ids):
    users = users_query().filter(id__in=ids)
    return Promise.resolve(reorder(ids, users))


def load_bands(ids):
    bands = bands_query().filter(id__in=ids)
    return Promise.resolve(reorder(ids, bands))


def load_albums(ids):
    albums = albums_query().filter(id__in=ids)
    return Promise.resolve(reorder(ids, albums))


def load_songs(ids):
    songs = songs_query().filter(id__in=ids)
    return Promise.resolve(reorder(ids, songs))


user_loader = DataLoader(load_users, cache=False)
band_loader = DataLoader(load_bands, cache=False)
album_loader = DataLoader(load_albums, cache=False)
song_loader = DataLoader(load_songs, cache=False)


