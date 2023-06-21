from django.urls import path

from app import views

urlpatterns = [
    path('', views.personal, name="personal"),
    path('jugadores/', views.jugadores, name="jugadores"),
    path('amigos/', views.amigos, name="amigos"),
    path('cosas/', views.cosas, name="cosas"),
    path('videos/', views.videos, name="videos"),

]
