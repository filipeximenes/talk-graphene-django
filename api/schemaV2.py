"""
Data loaders
"""

import graphene
from graphene_django.types import DjangoObjectType

from django.contrib.auth.models import User
from music_galery.models import Band, Album, Song
from .data_loaders import (
    users_query, bands_query, albums_query, songs_query,
    user_loader, band_loader, album_loader, song_loader
)


class UserType(DjangoObjectType):
    pk = graphene.Int()
    full_name = graphene.String(source='get_full_name')

    class Meta:
        model = User
        only_fields = (
            'full_name', 'bands')

    def resolve_bands(self, *args, **kwargs):
        return band_loader.load_many(
            [b.id for b in self.bands.all()])


class BandType(DjangoObjectType):
    pk = graphene.Int()

    class Meta:
        model = Band
        only_fields = (
            'name', 'artists', 'albums')

    def resolve_artists(self, *args, **kwargs):
        return user_loader.load_many(
            [a.id for a in self.artists.all()])

    def resolve_albums(self, *args, **kwargs):
        return album_loader.load_many(
            [a.id for a in self.albums.all()])


class AlbumType(DjangoObjectType):
    pk = graphene.Int()

    class Meta:
        model = Album
        only_fields = (
            'title', 'songs', 'release_date', 'band')

    def resolve_band(self, *args, **kwargs):
        return band_loader.load(self.band_id)

    def resolve_songs(self, *args, **kwargs):
        return song_loader.load_many(
            [s.id for s in self.songs.all()])


class SongType(DjangoObjectType):
    pk = graphene.Int()

    class Meta:
        model = Song
        only_fields = (
            'title', 'album')

    def resolve_album(self, *args, **kwargs):
        return band_loader.load(self.album_id)


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    bands = graphene.List(BandType)
    albums = graphene.List(AlbumType)
    songs = graphene.List(SongType)

    def resolve_users(self, info, **kwargs):
        return users_query

    def resolve_bands(self, info, **kwargs):
        return bands_query

    def resolve_albums(self, info, **kwargs):
        return albums_query

    def resolve_songs(self, info, **kwargs):
        return songs_query


schema = graphene.Schema(query=Query, auto_camelcase=False)
