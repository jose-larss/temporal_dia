from django.urls import path

from peliculas import views

urlpatterns = [
    path('', views.listar_peliculas, name="listar_peliculas"),
    path('insertar/', views.insertar_pelicula, name="insertar_pelicula"),
    path('formulario/', views.formulario, name="formulario"),

]