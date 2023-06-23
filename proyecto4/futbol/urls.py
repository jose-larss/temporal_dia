from django.urls import path

from futbol import views

urlpatterns = [
    path('',views.listar_jugadores, name="listar_jugadores"),

]