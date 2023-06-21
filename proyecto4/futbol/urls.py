from django.urls import path

from futbol import views

urlpatterns = [
    path('',views.index, name="listar_equipos"),

]