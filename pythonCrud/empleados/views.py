from django.shortcuts import render, redirect

from empleados.models import Empleado


"""
WEB CON MÉTODO GET


    • Desarrollar una web que nos muestre cinco hipervínculos con el texto de los distintos oficios de los empleados.
    • Enviar el nombre del oficio como parámetro en el hipervínculo.
    • Recoger con GET el dato que nos envían desde el formulario.
    • Mostrar los datos de los empleados del oficio pulsado.


"""

def empleados(request):
    empleado1 = Empleado()

    consulta = "select distinct oficio from emp"
    oficios, contador = empleado1.consultaBaseDatos(consulta, parametros=())

    return render(request, 'empleados/empleados.html', {'oficios':oficios})

def mostrar_empleados(request):
    empleado1 = Empleado()
    oficio = request.GET['oficio']

    consulta = "select apellido, oficio, salario from emp where oficio=:param1"
    personas, contador = empleado1.consultaBaseDatos(consulta, (oficio,))

    return render(request, 'empleados/mostrar_empleados.html', {'personas':personas})

def insertar_empleados(request):

    empleado1 = Empleado()
    if request.method != 'POST':

        return render(request, 'empleados/insertar_empleado.html')
    else:

        emp_no = request.POST['emp_no']
        apellido = request.POST['apellido']
        oficio= request.POST['oficio']
        dir= request.POST['dir']
        fecha= request.POST['fecha']
        salario= request.POST['salario']
        comision= request.POST['comision']
        dept_no= request.POST['dept_no']

        print(fecha)
        consulta = ("INSERT INTO EMP (emp_no,apellido,oficio, dir, fecha_alt, salario, comision, dept_no) VALUES (:P1, :P2, :P3,:P4, :P5, :P6,:P7, :P8)")
        contador = empleado1.consultaBaseDatos(consulta,(emp_no,apellido,oficio,dir,fecha,salario,comision,dept_no))

        return redirect('empleados')
