from django.db import models

import requests
from requests.exceptions import HTTPError

def consulta_Json(consulta):
    # esta es la url de star wars
    api_url = consulta
    try:
        # capturamos la respuesta
        response = requests.get(api_url)
        response.raise_for_status()
        print(f"El response raise for status es: {response.raise_for_status()}" )
        if response.status_code == 200:
            # convertimos la respuesta a objeto diccionario
            resultados = response.json()

        return resultados

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

    except Exception as err:
        print(f'Other error occurred: {err}')