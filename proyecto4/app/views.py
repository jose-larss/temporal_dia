from django.shortcuts import render

def personal(request):
    nombre = 'Jose luciano'
    apellido = 'castro'
    edad = 25

    return render(request, 'indice.html', {'nombre':nombre,
                                           'apellido':apellido,
                                           'edad':edad})


def jugadores(request):
    listajugadores=[
        {
            "Nombre":"Sergio Ramos",
            "Demarcacion":"Defensa",
            "Numero":5
        },
        {
            "Nombre": "Eden Hazard",
            "Demarcacion": "Delantero",
            "Numero":7
        },
        {
            "Nombre": "Karim Benzema",
            "Demarcacion": "Delantero",
            "Numero":9
        },
        {
            "Nombre": "Toni Kroos",
            "Demarcacion": "Centrocampista",
            "Numero":8
        },
        {
            "Nombre": "Thibaut Courtois",
            "Demarcacion": "Portero",
            "Numero": 1
        }
    ]

    contexto = {
        'listado_jugadores': listajugadores
    }
    return render(request, "Jugadores.html",contexto)

def amigos(request):

    listajugadores=[
        {
            "Nombre":"Sergio Ramos",
            "Demarcacion":"Defensa",
            "Numero":5
        },
        {
            "Nombre": "Eden Hazard",
            "Demarcacion": "Delantero",
            "Numero":7
        },
        {
            "Nombre": "Karim Benzema",
            "Demarcacion": "Delantero",
            "Numero":9
        },
        {
            "Nombre": "Toni Kroos",
            "Demarcacion": "Centrocampista",
            "Numero":8
        },
        {
            "Nombre": "Thibaut Courtois",
            "Demarcacion": "Portero",
            "Numero": 1
        }
    ]

    listaamigos=[
        {
            "Nombre":"Ana",
            "Demarcacion":"Defensa",
            "Numero":5
        },
        {
            "Nombre": "Andrea",
            "Demarcacion": "Delantero",
            "Numero":7
        },
        {
            "Nombre": "Adrian",
            "Demarcacion": "Delantero",
            "Numero":9
        },
        {
            "Nombre": "Lucia",
            "Demarcacion": "Centrocampista",
            "Numero":8
        },
        {
            "Nombre": "Marcos",
            "Demarcacion": "Portero",
            "Numero": 1
        }
    ]

    return render(request, 'amigos.html', {'lista_amigos':listaamigos,
                                           'lista_jugadores': listajugadores})

def cosas(request):
    return render(request, 'cosas.html')

def videos(request):
    return render(request, 'videos.html')
