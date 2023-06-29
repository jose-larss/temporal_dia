from django.shortcuts import render


def index(request):
    return render(request, "deportes/MultiplesAcciones.html")


def calcular(request):
    dato = request.POST['operacion']
    print(dato)
    try:
        num1 = int(request.POST['numero1'])
        num2 = int(request.POST['numero2'])

        if dato == 'sumarNumeros':
            resultado = num1 + num2
            operacion = "SUMA"
        elif dato == 'multiplicarNumeros':
            resultado = num1 * num2
            operacion = "MULTIPLICACIÓN"

    except ValueError:
        operacion = "La operación es erronea tienes que introducir Números "
        resultado = "NULO"

    lista = {
        "operacion": operacion,
        "resultado": resultado
    }

    return render(request, "deportes/MultiplesAcciones.html", lista)
