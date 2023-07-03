import requests
from Departamento import Departamento

class ConexionApiDepartamentos:
    def __init__(self):
        self.apiurl = "https://apicruddepartamentoscore.azurewebsites.net/";

    def insertarDepartamento(self, numero, nombre, localidad):
        request = "/api/departamentos"
        #CREAMOS UN OBJETO DEPARTAMENTO JSON
        # departamento = {"numero": numero, "nombre": nombre, "localidad": localidad}
        #CREAMOS NUESTRA URL CON LA PETICION
        url = self.apiurl + request;
        response = requests.post(url, json=departamento)
        return response.status_code;

    def modificarDepartamento(self, numero, nombre, localidad):
        request = "/api/departamentos"
        #CREAMOS UN OBJETO DEPARTAMENTO JSON PARA MODIFICAR
        departamento = {"numero": numero, "nombre": nombre, "localidad": localidad}
        #CREAMOS NUESTRA URL CON LA PETICION
        url = self.apiurl + request;
        response = requests.put(url, json=departamento)
        return response.status_code;

    def eliminarDepartamento(self, numero):
        request = "/api/departamentos/" + str(numero)
        #CREAMOS NUESTRA URL CON LA PETICION
        url = self.apiurl + request;
        response = requests.delete(url)
        return response.status_code;

    def buscarDepartamento(self, numero):
        request = "/api/departamentos/" + str(numero)
        url = self.apiurl + request;
        response = requests.get(url)
        if (response.status_code == 200):
            #capturamos la respuesta en json
            departamentojson = response.json()
            #Creamos un objeto de la clase Departamento para 
            #devolver la respuesta
            departamento = Departamento()
            departamento.numero = departamentojson["numero"]
            departamento.nombre = departamentojson["nombre"]
            departamento.localidad = departamentojson["localidad"]
            return departamento
        else:
            return None

    def todosDepartamentos(self):
        request = "/api/departamentos"
        url = self.apiurl + request;
        response = requests.get(url)
        #Creamos una lista para devolver todos los departamentos
        departamentos = []
        #capturamos la respuesta en json
        departamentojson = response.json()        
        for row in departamentojson:
            #Creamos un departamento por cada fila del bucle
            departamento = Departamento()
            #Asignamos los datos al nuevo objeto dept
            departamento.numero = row["numero"]
            departamento.nombre = row["nombre"]
            departamento.localidad = row["localidad"]
            #Añadimos a la lista cada nuevo objeto dept
            departamentos.append(departamento)
        return departamentos
