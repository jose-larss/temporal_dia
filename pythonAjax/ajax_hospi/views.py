from django.shortcuts import render

from ajax_hospi.models import Hospitales

def indice(request):
    return render(request, 'hospitales/indice_hospitales.html')

def vista_hospitales(request):
    hospi1 = Hospitales()

    consulta = "select * from hospital"
    hospitales = hospi1.consultaBaseDatos(consulta, parametros=())


    return render(request, 'hospitales/hospi.html', {'hospitales':hospitales})


def vista_doctores(request):
    hospi1 = Hospitales()

    consulta = "select * from doctor"
    doctores = hospi1.consultaBaseDatos(consulta, parametros=())


    return render(request, 'hospitales/doctores.html', {'doctores':doctores})


def vista_plantilla(request):
    hospi1 = Hospitales()

    consulta = "select * from plantilla"
    plantilla = hospi1.consultaBaseDatos(consulta, parametros=())


    return render(request, 'hospitales/plantilla.html', {'plantilla':plantilla})