from django.shortcuts import render
from empleado.models import Empleado

def index(request):

     return render(request, "inicio_empleado.html")

def empleados(request):
    estado = False
    ofi = request.POST['txtOficio']

    emple = Empleado()
    emple2 = Empleado()

    cursor = emple.devolverdato(ofi)
    cursor2 = emple2.devolverdato(ofi)

    for item in cursor2:
        print(item)

    print(estado)
    contexto = {

        'listado_empleados': cursor
    }

    return render(request, "segunda.html", contexto)
