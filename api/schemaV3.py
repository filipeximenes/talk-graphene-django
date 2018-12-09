"""
Relay and pagination
"""

import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType
from graphene_django.fields import DjangoConnectionField

from django.contrib.auth.models import User
from music_galery.models import Band, Album, Song
from .data_loaders import user_loader, band_loader, album_loader, song_loader


class UserType(DjangoObjectType):
    pk = graphene.Int()
    full_name = graphene.String(source='get_full_name')

    class Meta:
        model = User
        only_fields = (
            'full_name', 'bands')
        interfaces = (relay.Node,)

    def resolve_bands(self, *args, **kwargs):
        return band_loader.load_many(
            [b.id for b in self.bands.all()])


class BandType(DjangoObjectType):
    pk = graphene.Int()

    class Meta:
        model = Band
        only_fields = (
            'name', 'artists', 'albums')
        interfaces = (relay.Node,)

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
        interfaces = (relay.Node,)

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
        interfaces = (relay.Node,)

    def resolve_album(self, *args, **kwargs):
        return band_loader.load(self.album_id)


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    users = DjangoConnectionField(UserType)
    bands = DjangoConnectionField(BandType)
    albums = DjangoConnectionField(AlbumType)
    songs = DjangoConnectionField(SongType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_bands(self, info, **kwargs):
        return Band.objects.all()

    def resolve_albums(self, info, **kwargs):
        return Album.objects.all()

    def resolve_songs(self, info, **kwargs):
        return Song.objects.all()


schema = graphene.Schema(query=Query, auto_camelcase=False)
