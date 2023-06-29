from django.shortcuts import render

def index(request):
    return render(request, "gestion/Inicio.html")

def perso(request):
    listaPersonas = [
        {
            "nombre": "Benito",
            "apellido": "Floro",
        },
        {
            "nombre": "Andrea",
            "apellido": "Galindo",
        },
        {
            "nombre": "Thor",
            "apellido": "Ramiro",
        },
        {
            "nombre": "Alex",
            "apellido": "Galindo",
        },

    ]
    contexto = {
        'listado_Personas': listaPersonas
    }
    return render(request, "gestion/Personas.html", contexto)


def lenguaj(request):
    listaLenguajes = [
        {
            "nombre": "Python",
            "tipo": "Programación",
        },
        {
            "nombre": "SQL Server",
            "tipo": "Base de datos",
        },
        {
            "nombre": "C#",
            "tipo": "Programación",
        },
        {
            "nombre": "Java",
            "tipo": "Programación",
        },

    ]
    contexto = {
        'listado_Lenguajes': listaLenguajes
    }
    return render(request, "gestion/Lenguajes.html", contexto)
