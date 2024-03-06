# tomografo_api/urls.py
from django.urls import path
from .views import exame_list

urlpatterns = [
    path('exames/', exame_list, name='exame-list'),
]

