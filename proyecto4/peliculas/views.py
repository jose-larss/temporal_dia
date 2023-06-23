from django.shortcuts import render

from peliculas.models import  Pelicula


def formulario(request):
    return render(request, 'formulario.html')
def insertar_pelicula(request):
    pelicula = Pelicula()

    parametro = 25
    consulta = "select * from peliculas where IDPELICULA =:p1"
    dato = pelicula.ejecutar_crud_funcion(consulta, (parametro,))
    print(dato)
    return  render(request, 'insertar.html', {'dato':dato})

def listar_peliculas(request):
    pelicula = Pelicula()
    peliculas = pelicula.devolverpelicula()

    return render(request, 'peliculas.html', {'peliculas':peliculas})
