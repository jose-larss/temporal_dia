from django.urls import path

from multiplesAcciones import views

urlpatterns = [
    path('', views.index, name='index'),
    path('multiples', views.calcular, name='calcular'),
]