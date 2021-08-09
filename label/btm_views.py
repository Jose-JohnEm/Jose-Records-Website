from django.shortcuts import get_object_or_404, render
from .models import Prodbeat, ProdType

BASE_CONTEXT = {
        'nav_current': ['', '', '', 'active'],
        'page_name': "B.T.M Production",
        'iterable_name': 'ses prods :',
        'app_name': 'btm'
}

def get_complete_context(dict):
    iterables = [{**a.__dict__, **{'size': Prodbeat.objects.filter(genre=a).count()}} for a in ProdType.objects.all()]
    return {**BASE_CONTEXT, **{**{'iterable' : iterables}, **dict}}

def get_complete_context_with_genre(dict, genre):
    iterables = [a.__dict__ for a in ProdType.objects.all()]
    prods = [a for a in Prodbeat.objects.filter(genre=ProdType.objects.get(id=genre))]
    type_size = len(prods)
    type_name = ProdType.objects.get(id=genre).name
    return {**BASE_CONTEXT, **{**{'iterable' : iterables, 'prods': prods, 'type_name': type_name, 'type_size': type_size}, **dict}}


def btm_presentation(request):
    context = get_complete_context({})
    return render(request, 'label/btm.html', context)

def btm_types_presentation(request, type_id):
    context = get_complete_context_with_genre({}, type_id)
    return render(request, 'label/btm.html', context)

def btm_research(request):
    search = request.POST.get('btm-type-search')

    prods = Prodbeat.objects.filter(name__icontains=search)
    if prods.count() == 0:
        prods = Prodbeat.objects.filter(reference__icontains=search)
        if prods.count() == 0:
            prods = Prodbeat.objects.filter(genre__name__icontains=search)

    context = get_complete_context({
        'type_name': search,
        'research': True,
        'type_size': prods.count(),
        'prods': prods,
    })
    return render(request, 'label/btm.html', context)
