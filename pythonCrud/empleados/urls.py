from django.urls import path

from empleados import views

urlpatterns = [
    path('insertar/', views.insertar_empleados, name="insertar"),
    path('mostrar/', views.mostrar_empleados, name="mostrar"),
    path('', views.empleados, name="empleados"),
]