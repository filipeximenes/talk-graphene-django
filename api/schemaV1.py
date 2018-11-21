from django.db import models

import graphene
from graphene import relay
from graphene.types import Scalar
from graphene_django.converter import convert_django_field
from graphene_django.types import DjangoObjectType
from graphene_django.fields import DjangoConnectionField

from django.contrib.auth.models import User
from music_galery.models import Album, Song


class UserType(DjangoObjectType):
    pk = graphene.Int()
    full_name = graphene.String(source='get_full_name')

    class Meta:
        model = User
        only_fields = (
            'full_name', 'albums', 'composed_songs', 'produced_albums')


class BandType(DjangoObjectType):
    pk = graphene.Int()

    class Meta:
        model = Band
        only_fields = (
            'name', 'artists')

class AlbumType(DjangoObjectType):
    pk = graphene.Int()

    class Meta:
        model = Album
        only_fields = (
            'producer', 'title', 'release_date')


class SongType(DjangoObjectType):
    pk = graphene.Int()

    class Meta:
        model = Song
        only_fields = (
            'title', 'composer')


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    bands = graphene.List(BandType)
    albums = graphene.List(AlbumType)
    songs = graphene.List(SongType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()


schema = graphene.Schema(query=Query, auto_camelcase=False)