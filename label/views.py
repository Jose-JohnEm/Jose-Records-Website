from django.shortcuts import get_object_or_404, render
from .models import *

BASE_CONTEXT = {
        'nav_current': ['', 'active', '', ''],
        'page_name': "José Records",
        'iterable_name': 'les artistes passés par JR Services :',
        'app_name': 'label'
}

def get_complete_context(dict):
    return {**BASE_CONTEXT, **dict}

class ArtistListIterator():
    name = ''
    labeled = False
    picture = ''
    text = ''
    id = '-1'

def index(request):
    context = {
        'nav_current': ['active', '', '', ''],
        'page_name' : "Bienvenue"
    }
    return render(request, 'label/index.html', context)

def label_presentation(request):
    context = get_complete_context({
        'iterable' : [a.__dict__ for a in ArtistLabel.objects.all()],
    })

    return render(request, 'label/label.html', context)

def label_artist_presentation(request, artist_id):
    context = get_complete_context({
        'iterable' : [a.__dict__ for a in ArtistLabel.objects.all()],
        'artist': ArtistLabel.objects.get(id=artist_id),
        'active_iterator': artist_id,
    })
    return render(request, 'label/label.html', context)