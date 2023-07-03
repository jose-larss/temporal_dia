from ConexionApiDepartamentos import ConexionApiDepartamentos

print("DEPARTAMENTOS API CON CLASES")
#Creamos el objeto conexion para trabajar
connection = ConexionApiDepartamentos()
opcion = -1
while (opcion != 6):
    print("------------MENU-----------")
    print("1.- Nuevo Departamento")
    print("2.- Eliminar departamento")
    print("3.- Modificar departamento")
    print("4.- Buscar departamento")
    print("5.- Mostrar departamentos")
    print("6.- Salir")
    print("Seleccione un opción")
    opcion = int(input())
    if (opcion == 1):
        print("-----INSERTANDO-----")
        print("Introduzca un número")
        numero = int(input())
        print("Introduzca un nombre")
        nombre = input()
        print("Introduzca una localidad")
        localidad = input()
        respuesta = connection.insertarDepartamento(numero, nombre, localidad)
        print("Departamentos insertados " + str(respuesta))
    elif (opcion == 2):
        print("-----ELIMINANDO-----")
        print("Número de departamento a eliminar")
        numero = int(input())
        respuesta = connection.eliminarDepartamento(numero)
        print("Departamentos eliminados: " + str(respuesta))
    elif (opcion == 3):
        #Llamamos a modificar
        print("-----Update------")
        print("Introduzca número de departamento")
        numero = int(input())
        print("Introduzca nuevo nombre")
        nombre = input()
        print("Introduzca nueva localidad")
        localidad = input()
        respuesta = connection.modificarDepartamento(
            numero, nombre, localidad)
        print("Departamentos modificados: " + str(respuesta))
    elif (opcion == 4):
        print("Introduzca número departamento")
        numero = int(input())
        #Se supone que nos tiene que devoler un departamento
        #o nada...
        departamento = connection.buscarDepartamento(numero)
        if (not departamento):
            print("No existe el departamento")
        else:
            print(departamento)
    elif (opcion == 5):
        #Recuperamos la lista de departamentos
        departamentos = connection.todosDepartamentos()
        for dept in departamentos:
            print(dept)
    elif (opcion == 6):
        print("Hasta luego")
    else:
        print("Opción incorrecta")
print("Fin de programa")