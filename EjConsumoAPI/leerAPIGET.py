import requests
import json


api_url = "https://apiempleadosspgs.azurewebsites.net/api/Empleados"
#capturamos la respuesta
response = requests.get(api_url)
#convertimos la respuesta a objeto diccionario
empleados = response.json()
print("Listado empleados")
print("-------------------")
for i in empleados:
    print(i)
    print(i["apellido"])