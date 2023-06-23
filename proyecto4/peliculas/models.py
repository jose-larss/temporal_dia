from django.db import models

import cx_Oracle

class Pelicula:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
        self.cursor = self.connection.cursor()

    def devolverpelicula(self):

        try:
            self.cursor.execute("select titulo, foto, argumento from peliculas")
        except self.connection.Error as error:
            print("Error: ", error)

        return self.cursor

    def devolverpelicula_funcion(self, consulta):

        try:
            self.cursor.execute(consulta)
        except self.connection.Error as error:
            print("Error: ", error)

        return self.cursor

    def ejecutar_crud_funcion(self, consulta, parametros = ()):
        print(consulta)
        print(parametros)
        try:
            self.cursor.execute(consulta, parametros)
        except self.connection.Error as error:
            print("Error: ", error)

        return self.cursor

