from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('', views.art, name = 'art'),
    path('', views.physics, name = 'physics'),
    path('', views.dance, name = 'dance')
]

