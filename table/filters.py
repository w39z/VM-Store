import django_filters

from table.models import *


class ItemFilter(django_filters.FilterSet):

    class Meta:
        model = Item
        fields = '__all__'
