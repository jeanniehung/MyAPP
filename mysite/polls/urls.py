from django.urls import path
from . import views


urlpattrens = [
    path('', views.index, name='index'),
]