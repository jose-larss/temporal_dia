from django.shortcuts import render, redirect
from django.contrib import messages

from crud.models import Departamento

def index(request):
    dept = Departamento()

    consulta = ("SELECT * FROM dept order by dept_no")
    departamentos, contador = dept.consultaBaseDatos(consulta,  parametros = ())

    return render(request, 'crud/indice.html', {'departamentos':departamentos})


def alta_dept(request):

    if request.method != 'POST':
        return render(request,'crud/alta.html')
    else:
        dept = Departamento()

        departamento = request.POST['departamento']
        nombre = request.POST['nombre']
        localidad = request.POST['localidad']

        consulta = ("INSERT INTO dept (dept_no,dnombre,loc) VALUES (:P1, :P2, :P3)")

        departamentos, contador = dept.consultaBaseDatos(consulta, (departamento, nombre, localidad))

        if contador > 0:
            messages.success(request,f"Enhorabuena has insertado un registro {departamento} {nombre} {localidad}")
        else:
            messages.error(request, f"Error el Registro existe!! MODIFICALO")

        return redirect('indice') #, mensaje=mensaj

def leer_departamentos(request):
    dept = Departamento()

    departamentos, contador= dept.consultaBaseDatos()

    return render(request, 'crud/leer.html', {'departamentos':departamentos})

def baja_departamento(request, id_baja):

    dept = Departamento()

    #departamentos = dept.lectura_departamento()
    """
    if request.method != 'POST':
        return render(request, 'crud/baja.html', {'departamentos':departamentos})
    else
    """
    #codigo = int(request.POST['codigo'])
    #print(type(codigo))
    consulta = ("Delete from dept where dept_no=:param1")
    departamentos, contador = dept.consultaBaseDatos(consulta, (id_baja,))

    messages.error(request, f"Enhorabuena has borrado el departamento número {id_baja}")

    return redirect('indice')

def modificar_departamento(request, id_mod):

    dept = Departamento()
    consulta = ("select * from dept where dept_no=:param1")
    departamento, contador = dept.consultaBaseDatos(consulta, (id_mod,))

    for dept in departamento:
        pass
    if request.method != 'POST':
        return render(request, 'crud/modificar.html', {'departamento':dept})
    else:
        #codigo = request.POST['codigo']
        localidad = request.POST['localidad']
        #print(request.POST['codigo'])
        print(request.POST['localidad'])
        dept2 = Departamento()
        consulta = ("Update dept set loc=:Param1 where dept_no=:Param2")
        departamentos, contador = dept2.consultaBaseDatos(consulta, (localidad, id_mod))

        messages.success(request, f"Enhorabuena has Modificado el departamento numero: {id_mod} nombre: {dept[1]} localidad: {localidad}")
        return redirect('indice')
