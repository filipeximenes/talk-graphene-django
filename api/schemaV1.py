"""
Basic querying and custom scalars
"""

import graphene
from graphene_django.types import DjangoObjectType

from django.contrib.auth.models import User
from music_galery.models import Band, Album, Song


# class Date(graphene.Date):

#     @staticmethod
#     def serialize(dt):
#         return dt.strftime('%m/%Y')


class UserType(DjangoObjectType):
    pk = graphene.Int()
    full_name = graphene.String(source='get_full_name')

    class Meta:
        model = User
        only_fields = (
            'full_name', 'bands')


class BandType(DjangoObjectType):
    pk = graphene.Int()

    class Meta:
        model = Band
        only_fields = (
            'name', 'artists', 'albums')


class AlbumType(DjangoObjectType):
    pk = graphene.Int()
    # release_date = Date()

    class Meta:
        model = Album
        only_fields = (
            'title', 'songs', 'release_date', 'band')


class SongType(DjangoObjectType):
    pk = graphene.Int()

    class Meta:
        model = Song
        only_fields = (
            'title', 'album')


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    bands = graphene.List(BandType)
    albums = graphene.List(AlbumType)
    songs = graphene.List(SongType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_bands(self, info, **kwargs):
        return Band.objects.all()

    def resolve_albums(self, info, **kwargs):
        return Album.objects.all()

    def resolve_songs(self, info, **kwargs):
        return Song.objects.all()


schema = graphene.Schema(query=Query, auto_camelcase=False)
