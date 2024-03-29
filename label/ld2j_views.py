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
    album = LD2JAlbum.objects.get(id=album_id)
    ctb = ", ".join([c.name for c in album.contributors.all()])
    tmp_titles = album.musics.all()
    final_titles = []

    for ti in tmp_titles:
        if ti.contributors.all().count() != 0:
            contri = [t.name for t in ti.contributors.all()]
            final_titles += [ti.name + " (ft. " + " & ".join(contri) + ")"]
        else:
            final_titles += [ti.name]

    ctb = ctb[:ctb.rfind(", ")] + " et " + ctb[ctb.rfind(", ") + 2:]
    context = get_complete_context({
        'album': album,
        'titles': final_titles,
        'contributors': ctb,
    })
    return render(request, 'label/ld2j.html', context)