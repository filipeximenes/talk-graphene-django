from promise.dataloader import DataLoader

from django.contrib.auth.models import User
from music_galery.models import Band, Album, Song


def reorder(ordered_ids, items):
    items_dict = {i.id: i for i in items}
    return [items_dict[i] for i in ordered_ids]


def load_users(ids):
    users = User.objects.filter(id__in=ids)
    return reorder(ids, users)


def load_bands(ids):
    bands = Band.objects.filter(id__in=ids)
    return reorder(ids, bands)


def load_albums(ids):
    albums = Album.objects.filter(id__in=ids)
    return reorder(ids, albums)


def load_songs(ids):
    songs = Song.objects.filter(id__in=ids)
    return reorder(ids, songs)


user_loader = DataLoader(load_users, cache=False)
band_loader = DataLoader(load_bands, cache=False)
album_loader = DataLoader(load_albums, cache=False)
song_loader = DataLoader(load_songs, cache=False)
