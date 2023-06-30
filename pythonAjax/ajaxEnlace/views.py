from django.shortcuts import render

def inicio(request):
    return render(request, "gestion/Index.html")

def verdatos(request):
    datoget = request.GET["id"]
    datoget2 = request.GET["nombre"]
    print(datoget, datoget2)
    contexto = {
        'dato1': datoget,
        'dato2': datoget2

    }
    return render(request, "gestion/verdatos.html",contexto)
