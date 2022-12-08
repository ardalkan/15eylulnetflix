from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='index' ),
    path('movies/<str:profilIsim>/<str:profilid>/',movies, name='movies'),
    path('video/<int:filmId>',video,name="video")
]