from django.shortcuts import render, redirect
from django.contrib import messages

from crud.models import Departamento

def index(request):
    men = ""
    dept = Departamento()
    consulta = "SELECT * FROM dept order by dept_no"
    #departamentos = dept.lectura_departamento()
    departamentos, contador = dept.lectura_departamento(consulta, param=())

    return render(request, 'crud/indice.html', {'departamentos':departamentos,
                                                'men':men})


def alta_dept(request):

    if request.method != 'POST':
        return render(request,'crud/alta.html')
    else:
        dept = Departamento()
        departamento = request.POST['departamento']
        nombre = request.POST['nombre']
        localidad = request.POST['localidad']

        consulta = ("INSERT INTO dept (dept_no,dnombre,loc) VALUES (:P1, :P2, :P3)")

        departamentos, contador = dept.lectura_departamento(consulta, (departamento, nombre, localidad))
        if contador > 0:
            messages.success(request,f"Enhorabuena has insertado un registro", extra_tags='success')
        else:
            messages.error(request,f"Error Ora-0001 Unique constraint Violated", extra_tags='error' )

        return redirect('indice') #, mensaje=mensaj

def leer_departamentos(request):
    dept = Departamento()
    consulta = "SELECT * FROM dept order by dept_no"

    departamentos,contador = dept.lectura_departamento(consulta)

    return render(request, 'crud/leer.html', {'departamentos':departamentos})

def baja_departamento(request, id_borrar):

    dept = Departamento()
    consulta = ("Delete from dept where dept_no=:param1")
    departamento, contador = dept.lectura_departamento(consulta, (id_borrar,))

    messages.success(request, f"Enhorabuena has borrado el departamento numero {id_borrar}", extra_tags='success')

    return redirect('indice')

def modificar_departamento(request, id_modi):

    dept = Departamento()
    consulta = ("SELECT * FROM dept where dept_no=:param1")
    dept, contador = dept.lectura_departamento(consulta,(id_modi,))

    for item in dept:
        pass

    if request.method != 'POST':
        return render(request, 'crud/modificar.html', {#'departamentos':departamentos, 
                                                        'dept':item})
    
    else:
        dept2 = Departamento()

        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        localidad = request.POST['localidad']

        consulta = ("Update dept set loc=:Param1, dnombre=:Param2  where dept_no=:Param3")

        departamentos, contador = dept2.lectura_departamento(consulta, (localidad, nombre ,codigo))

        messages.success(request, f"Enhorabuena has Modificado el departamento a {codigo} {nombre} {localidad}", extra_tags='success')
        return redirect('indice')
    
