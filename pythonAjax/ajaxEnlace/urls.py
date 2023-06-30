from django.urls import path

from ajaxEnlace import views


urlpatterns=[
    path('inicio', views.inicio, name='inicio'),
    path('Recuperar', views.verdatos, name='verdatos')
]