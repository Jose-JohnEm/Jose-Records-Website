from django.urls import path

from . import views

urlpatterns = [
    path('', views.label_presentation, name='label_presentation'),
    path('<int:artist_id>', views.label_artist_presentation, name='label_artist_presentation'),
]
