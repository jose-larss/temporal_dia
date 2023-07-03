"""
import requests
import json


api_url = "https://apiempleadosspgs.azurewebsites.net/api/Empleados/7900"
#capturamos la respuesta
response = requests.get(api_url)
#convertimos la respuesta a objeto diccionario
empleado = response.json()
print(empleado)
print(empleado["apellido"])
print(empleado['oficio'])
"""
import requests
from requests.exceptions import HTTPError

    # EJEMPLO PETICIÓN API CENTROS DE DÍA

api_url = "https://datos.madrid.es/egob/catalogo/200342-0-centros-dia.json"
try:
    response = requests.get(api_url)
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    for i in jsonResponse['@graph']:
        print(i['title'])

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')