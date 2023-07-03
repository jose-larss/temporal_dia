
from django.urls import path

from starWars import views

urlpatterns = [
    path('', views.listar_personajes, name="listar"),
]