from django.urls import path

from empleado import views

urlpatterns = [

    path('', views.index, name='index_empleado'),
    path('empleados2/', views.empleados, name='empleados'),

]