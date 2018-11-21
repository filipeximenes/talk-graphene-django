from datetime import date
from model_mommy import mommy
from django.conf import settings
from django.contrib.auth.models import User
from music_galery.models import Band, Album, Song


User.objects.all().delete()
Band.objects.all().delete()
Album.objects.all().delete()
Song.objects.all().delete()


# Users

siba = mommy.make(
    settings.AUTH_USER_MODEL,
    first_name='Siba',
    last_name='Veloso')
fabio = mommy.make(
    settings.AUTH_USER_MODEL,
    first_name='Fábio',
    last_name='Trumer')
urea = mommy.make(
    settings.AUTH_USER_MODEL,
    first_name='Alexandre',
    last_name='Urêa')
gilu = mommy.make(
    settings.AUTH_USER_MODEL,
    first_name='Gilú',
    last_name='Amaral')
juliano = mommy.make(
    settings.AUTH_USER_MODEL,
    first_name='Juliano',
    last_name='Holanda')
tine = mommy.make(
    settings.AUTH_USER_MODEL,
    first_name='Tiné')
salu = mommy.make(
    settings.AUTH_USER_MODEL,
    first_name='Maciel',
    last_name='Salu')
yuri = mommy.make(
    settings.AUTH_USER_MODEL,
    first_name='Yuri',
    last_name='Rabid')
hugo = mommy.make(
    settings.AUTH_USER_MODEL,
    first_name='Hugo',
    last_name='Gila')


def setup_band(name, artists, albums):
    band = mommy.make(
        'music_galery.Band',
        name=name)

    band.artists.add(*artists)

    for album_info in albums:
        album = mommy.make(
            'music_galery.Album',
            band=band,
            title=album_info['title'],
            release_date=date(year=album_info['year'], month=1, day=1))

        for song in album_info['songs']:
            mommy.make(
                'music_galery.Song',
                album=album,
                title=song)
        


# Bands

setup_band(
    'Siba', 
    [siba],
    [
        {
            'title': 'Fuloresta do Samba',
            'year': 2002,
            'songs': [
                'Fuloresta do Samba',
                'Bringa',
                'Caluanda',
                'Suinã',
                'Bonina',
            ]
        },
        {
            'title': 'Toda Vez Que Eu Dou Um Passo O Mundo Sai Do Lugar',
            'year': 2007,
            'songs': [
                'Pisando em Praça de Guerra',
                'Cantar Ciranda',
                'Meu Time',
                'Será?',
                'Alados',
            ]
        },
    ]
)

setup_band(
    'Eddie', 
    [fabio, urea],
    [
        {
            'title': 'Original Olinda Style',
            'year': 2002,
            'songs': [
                'Fuloresta do Samba',
                'Bringa',
                'Caluanda',
                'Suinã',
                'Bonina',
            ]
        },
        {
            'title': 'Metropolitano',
            'year': 2006,
            'songs': [
                'Pisando em Praça de Guerra',
                'Cantar Ciranda',
                'Meu Time',
                'Será?',
                'Alados',
            ]
        },
        {
            'title': 'Carnaval no Inferno',
            'year': 2008,
            'songs': [
                'Pisando em Praça de Guerra',
                'Cantar Ciranda',
                'Meu Time',
                'Será?',
                'Alados',
            ]
        },
        {
            'title': 'Mundo Engano',
            'year': 2018,
            'songs': [
                'Pisando em Praça de Guerra',
                'Cantar Ciranda',
                'Meu Time',
                'Será?',
                'Alados',
            ]
        },
    ]
)

setup_band(
    'Orquestra Contemporânea de Olinda', 
    [gilu, hugo, juliano, tine, salu],
    [
        {
            'title': 'Orquestra Contemporânea de Olinda',
            'year': 2008,
            'songs': [
                'Fuloresta do Samba',
                'Bringa',
                'Caluanda',
                'Suinã',
                'Bonina',
            ]
        },
        {
            'title': 'Pra ficar',
            'year': 2012,
            'songs': [
                'Pisando em Praça de Guerra',
                'Cantar Ciranda',
                'Meu Time',
                'Será?',
                'Alados',
            ]
        },
        {
            'title': 'Bomfim',
            'year': 2017,
            'songs': [
                'Pisando em Praça de Guerra',
                'Cantar Ciranda',
                'Meu Time',
                'Será?',
                'Alados',
            ]
        },
    ]
)

setup_band(
    'Academia da Berlinda', 
    [tine, urea, yuri, hugo],
    [
        {
            'title': 'Academia da Berlinda',
            'year': 2007,
            'songs': [
                'Fuloresta do Samba',
                'Bringa',
                'Caluanda',
                'Suinã',
                'Bonina',
            ]
        },
        {
            'title': 'Olindance',
            'year': 2008,
            'songs': [
                'Pisando em Praça de Guerra',
                'Cantar Ciranda',
                'Meu Time',
                'Será?',
                'Alados',
            ]
        },
        {
            'title': 'Nada Sem Ela',
            'year': 2016,
            'songs': [
                'Pisando em Praça de Guerra',
                'Cantar Ciranda',
                'Meu Time',
                'Será?',
                'Alados',
            ]
        },
    ]
)
