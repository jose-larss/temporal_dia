from django.shortcuts import render, redirect

from mult_acciones1.models import Departamento
def inicio(request):
    mensaje = ""
    dept1 = Departamento()

    if request.method != 'POST':

        consulta = "select * from dept order by dept_no"
        departamentos, contador, error = dept1.consultaBaseDatos(consulta, parametros=())
        contexto = {
            'departamentos': departamentos,
        }
        #return render(request, 'departamentos/inicio_departamentos.html', {'departamentos':departamentos})
    else:

        codigo = request.POST['numero']
        nombre = request.POST['nombre']
        localidad = request.POST['localidad']

        opcion = request.POST['opcion']

        if opcion == 'insertar':
            consulta = ("INSERT INTO dept (dept_no,dnombre,loc) VALUES (:param1, :param2, :param3)")
            cursor , contador, error = dept1.consultaBaseDatos(consulta, (codigo, nombre, localidad))
            if contador > 0:
                mensaje = f"Registros Insertados {contador} , Nº departamento:{codigo} - {nombre} : {localidad}"
            else:
                mensaje = error

        elif opcion == 'modificar':
            consulta = ("Update dept set dnombre=:param1, loc=:param2 where dept_no=:Param3")
            cursor, contador, error = dept1.consultaBaseDatos(consulta,(nombre, localidad, codigo))
            if contador > 0:
                mensaje = f"Registros modificados {contador}, Nº departamento:{codigo} a {nombre} y {localidad}"
            else:
                mensaje = f"Registros Modificados 0"

        elif opcion == 'eliminar':
            consulta = ("delete from dept where dept_no=:param1")
            cursor, contador, error = dept1.consultaBaseDatos(consulta,(codigo,))
            if contador > 0:
                mensaje = f"Registros Borrados {contador}, Nº departamento: {codigo}"
            else:
                mensaje = f"Registros Borrados 0"
        # Tiene que estar aqui para en el caso que haga algo que actualice en tiempo real
        consulta = "select * from dept order by dept_no"
        departamentos, contador, error = dept1.consultaBaseDatos(consulta, parametros=())
        print(contador)
        contexto = {
            'mensaje': mensaje,
            'departamentos': departamentos,
        }
    return render(request, 'departamentos/inicio_departamentos.html',contexto)