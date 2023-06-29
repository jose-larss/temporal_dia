from django.urls import path

from tailProject import views

urlpatterns = [

    path('', views.tail_indice, name="indice"),
    #path('procesar/', views.procesarFormulario, name="procesar"),
    #path('borrar/<str:nom_borrar>/', views.borrar, name="borrar"),
]