import requests

apiurl = "https://apicruddepartamentoscore.azurewebsites.net"
request = "/api/departamentos"
departamento = {"numero": 7, "nombre": "James Bond ", "localidad": "reino unido"}

response = requests.post(apiurl + request, json=departamento)
#convertimos la respuesta a objeto diccionario
#print(response.json())
print("Status: " + str(response.status_code))