from django.urls import path

from . import views

urlpatterns = [
    path('add', views.create, name='create'),
    path('list', views.index, name='index')
]
