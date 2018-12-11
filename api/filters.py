from django_filters import FilterSet, filters

from music_galery.models import Band


class BandFilterSet(FilterSet):

    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Band
        fields = []