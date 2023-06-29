from django.urls import path

from mult_acciones1 import views

urlpatterns = [
    path('', views.inicio, name="inicio_multiples"),
]