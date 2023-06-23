from django.shortcuts import render
from futbol.models import Jugador


def listar_jugadores(request):
    #Instancias la clase
    jugador = Jugador()
    equipo = Jugador()

    #llamada al metodo de la clase devolverDato()
    jugadores =jugador.devolverdato()
    consulta = "SELECT * FROM equipos"
    equipos = equipo.devolverdato_funcion(consulta)
    print(equipos)

    contexto = {
        'listado_jugadores': jugadores,
        'listado_equipos':equipos,
    }
    return render(request, "JugadoresPrimera.html", contexto)
