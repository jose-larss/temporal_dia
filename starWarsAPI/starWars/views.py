from django.shortcuts import render

from starWars.models import consulta_Json

def listar_personajes(request):

    # esta es la url de star wars
    consulta = "https://swapi.dev/api/people/"
    personajes = consulta_Json(consulta)

    return render(request, 'starwars/listado.html', {'personajes':personajes})

def detalle(request):
    return render(request, 'starwars/listado.html')




