import requests
from requests.exceptions import HTTPError


apiurl = "https://apiempleadosspgs.azurewebsites.net/api/Empleados/7840"
try:
    response = requests.get(apiurl)
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')