from django.shortcuts import get_object_or_404, render
from .models import *

BASE_CONTEXT = {
        'nav_current': ['', '', 'active', ''],
        'page_name': "LD2J",
        'iterable_name': 'ses albums :',
        'app_name': 'ld2j'
}

def get_complete_context(dict):
    iterables = [a.__dict__ for a in LD2JAlbum.objects.all()]
    return {**BASE_CONTEXT, **{**{'iterable' : iterables}, **dict}}

def index(request):
    context = get_complete_context({})
    return render(request, 'label/ld2j.html', context)

def ld2j_album_presentation(request, album_id):
    context = get_complete_context({
        'album': LD2JAlbum.objects.get(id=album_id),
        'titles': LD2JAlbum.objects.musics.all(),
    })
    return render(request, 'label/ld2j.html', context)