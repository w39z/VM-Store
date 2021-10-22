from django.shortcuts import render
from table.filters import *


def index(request):
    items = Item.objects.all()
    filter = ItemFilter(request.GET, queryset=items)
    items = filter.qs

    return render(request, 'index.html',
           {'items': items,
            'filter': filter})




