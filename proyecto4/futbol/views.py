from django.shortcuts import render
from futbol.models import Jugador


def index(request):
    #Instancias la clase
    emple = Jugador()
    #llamada al metodo de la clase devolverDato()
    cursor=emple.devolverdato()

    contexto = {
        'listado_empleados': cursor
    }
    return render(request, "JugadoresPrimera.html", contexto)
