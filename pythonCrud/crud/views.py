from django.shortcuts import render, redirect
from django.contrib import messages

from crud.models import Departamento

def index(request):
    men = ""
    dept = Departamento()
    departamentos = dept.lectura_departamento()

    return render(request, 'crud/indice.html', {'departamentos':departamentos,
                                                'men':men})


def alta_dept(request):

    if request.method != 'POST':
        return render(request,'crud/alta.html')
    else:

        departamento = request.POST['departamento']
        nombre = request.POST['nombre']
        localidad = request.POST['localidad']

        dept = Departamento()

        departamentos = dept.insertar_departamento(departamento, nombre, localidad)
        messages.success(request, f"Enhorabuena has insertado un registro")

        return redirect('indice') #, mensaje=mensaj

def leer_departamentos(request):
    dept = Departamento()

    departamentos = dept.lectura_departamento()

    return render(request, 'crud/leer.html', {'departamentos':departamentos})

def baja_departamento(request):

    dept = Departamento()

    departamentos = dept.lectura_departamento()
    if request.method != 'POST':
        return render(request, 'crud/baja.html', {'departamentos':departamentos})
    else:
        codigo = int(request.POST['codigo'])
        print(type(codigo))
        dept = Departamento()

        departamentos = dept.borrar_departamento(codigo)

        messages.success(request, f"Enhorabuena has borrado el departamento")

        return redirect('indice')

def modificar_departamento(request):

    dept = Departamento()
    departamentos = dept.lectura_departamento()

    if request.method != 'POST':
        return render(request, 'crud/modificar.html', {'departamentos':departamentos})
    else:
        codigo = request.POST['codigo']
        localidad = request.POST['localidad']
        print(request.POST['codigo'])
        print(request.POST['localidad'])

        dept = Departamento()

        departamentos = dept.modificar_departamento(localidad, codigo)

        messages.success(request, f"Enhorabuena has Modificado el departamento")
        return redirect('indice')
