from django.shortcuts import render
from parametrosAjax.models import Hospitales
def inicio(request):
    hospital = Hospitales()
    consulta = "select * from hospital"
    hospitales = hospital.consultaBaseDatos(consulta, parametros=())
    hospitales2 = hospital.consultaBaseDatos(consulta, parametros=())

    return render(request, 'parametros/inicio.html', {'hospitales':hospitales,
                                                      'hospitales2':hospitales2})

def plantilla(request):

    hospital = Hospitales()
    id = request.GET['id']
    consulta = "select * from plantilla where hospital_cod=:param1"
    plantilla = hospital.consultaBaseDatos(consulta, (id,))

    return render(request, 'parametros/segunda.html', {'plantilla':plantilla})

def plantilla2(request):

    hospital = Hospitales()
    id = request.GET['id']
    print(id)
    consulta = "select * from plantilla where hospital_cod=:param1"
    plantilla = hospital.consultaBaseDatos(consulta, (id,))

    return render(request, 'parametros/segunda2.html', {'plantilla':plantilla})