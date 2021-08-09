from django.urls import path

from . import label_views
from . import ld2j_views
from . import btm_views

label_patterns = [
    path('label/', label_views.label_presentation, name='label_presentation'),
    path('label/<int:artist_id>', label_views.label_artist_presentation, name='label_artist_presentation'),
]

ld2j_patterns = [
    path('ld2j/', ld2j_views.index, name='ld2j_presentation'),
    path('ld2j/<int:album_id>', ld2j_views.ld2j_album_presentation, name='ld2j_album_presentation'),
]

btm_patterns = [
    path('btm/', btm_views.btm_presentation, name='btm_presentation'),
    path('btm/<int:type_id>', btm_views.btm_types_presentation, name='btm_types_presentation'),
    path('btm/search', btm_views.btm_research, name='btm_research'),
]

urlpatterns = label_patterns + ld2j_patterns + btm_patterns