from django.urls import path

from hospital import views

urlpatterns = [
    path('', views.hospital, name="hospital"),

]