from django.shortcuts import render

from hospital.models import Hospital
def hospital(request):
    hospi = Hospital()
    stringSo = ""

    consulta = ("select * from hospital")
    hospitales, contador = hospi.consultaBaseDatos(consulta, parametros=())

    if request.method != 'POST':
        return render(request, 'hospital/hospital.html', {'hospitales':hospitales})
    else:
        #hospi2 = Hospital()
        #lista_doctores = []

        lista_hospitales = request.POST.getlist('chkHospi')

        #consulta_hospital = "select * from doctor where hospital_cod in(15,22,45)"
        stringSo = ','.join(lista_hospitales)
        consulta_hospital = "select * from doctor where hospital_cod in(" + stringSo + ")"

        doctores, contador = hospi.consultaBaseDatos(consulta_hospital)
        print(contador)

        """
        for item in lista_hospitales:
            hospi2 = Hospital()


            consulta_hospital = "select * from doctor where hospital_cod=:param1"
            doctores, contador = hospi2.consultaBaseDatos(consulta_hospital, (int(item),))
            print(doctores)
            for doctor in doctores:
                lista_doctores.append([doctor[2], doctor[3], doctor[4]])

        print(lista_doctores)
        """

        return render(request, 'hospital/hospital.html', {'hospitales':hospitales,
                                                          'doctores':doctores})

def datosDoctores(request):
    doc = Doctor()
    Nombhospitales = doc.nombreshosp()

    checkrecogidos = request.POST.getlist('hospital')
    #Comprobamos si la lista no está vacía. Si existe.
    if checkrecogidos:
        listadoDoct = doc.doctoreshosp(checkrecogidos)
        datos = {
            'hospi': Nombhospitales,
            'listado': listadoDoct,
        }
        # Si está vacía o es la primera vez no enviamos el listado de doctores
    else:
        datos = {
            'hospi': Nombhospitales,
        }

    return render(request, 'gestion/index.html', datos)

