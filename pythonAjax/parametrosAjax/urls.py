from django.urls import path

from parametrosAjax import views

urlpatterns=[
    path('', views.inicio, name='inicio'),
    path('plantilla/', views.plantilla, name='plantilla'),
    path('plantilla2/', views.plantilla2, name='plantilla2'),
]