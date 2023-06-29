from django.urls import path

from ajax_hospi import views

urlpatterns=[

    path('',views.indice,name='index'),
    path('plantilla',views.vista_plantilla,name='plantilla'),
    path('hospitales',views.vista_hospitales,name='hospitales'),
    path('doctores',views.vista_doctores,name='doctores'),
]