from django.shortcuts import render, redirect

from cliente.models import Cliente

def indice(request):
    return render(request, 'cliente/formulario.html')


def borrar(request, nom_borrar):
    cliente = Cliente()

    consulta = "delete from clientesAlumnos where nombre=:param1"

    cliente.consultaBaseDatos(consulta, (nom_borrar,))

    return redirect('procesar')
def procesarFormulario(request):
    cliente = Cliente()
    stringSo = ""

    if request.method != 'POST':
        return render(request, 'cliente/procesado.html')
    else:

        nombre = request.POST['nombre']
        primer = request.POST['primer']
        segundo = request.POST['segundo']
        domicilio = request.POST['domicilio']
        ciudad = request.POST['ciudad']
        sexo = request.POST['sexo']
        so = request.POST.getlist('so')
        #Uso de join########
        stringSo = ','.join(so)
        #print(stringSo)

        area = request.POST['area']
        """
        print(nombre)
        print(primer)
        print(segundo)
        print(domicilio)
        print(ciudad)
        print(sexo)
        print(so)
        print(area)
        """

        consulta = """INSERT INTO clientesAlumnos  (NOMBRE ,APELLIDO1 ,APELLIDO2,DOMICILIO, CIUDAD, SEXO, SISTEMA, COMENTARIOS ) 
        VALUES (:P1, :P2, :P3,:P4, :P5, :P6,:P7, :P8)"""
        cliente.consultaBaseDatos(consulta, (nombre, primer, segundo, domicilio, ciudad, sexo, stringSo, area))

        consulta2 = "select * from clientesAlumnos"
        clientes, contador = cliente.consultaBaseDatos(consulta2, parametros = ())

        return render(request, 'cliente/procesado.html', {'clientes':clientes})


