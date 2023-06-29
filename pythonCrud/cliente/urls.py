from django.urls import path

from cliente import views

urlpatterns = [
    path('', views.indice, name="indice"),
    path('procesar/', views.procesarFormulario, name="procesar"),
    path('borrar/<str:nom_borrar>/', views.borrar, name="borrar"),
]