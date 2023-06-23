from django.urls import path

from crud import views

urlpatterns = [
    path('modificar/', views.modificar_departamento, name="modificar"),
    path('baja/', views.baja_departamento, name="baja"),
    path('leer/', views.leer_departamentos, name="leer"),
    path('alta/', views.alta_dept, name="alta"),
    path('',views.index, name="indice"),
]