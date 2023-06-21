from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    respuesta = request.user
    print(request)

    return render(request, "gestion/inicio.html", {'respuesta': respuesta})
