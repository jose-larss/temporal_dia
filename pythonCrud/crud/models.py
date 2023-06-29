from django.db import models

import cx_Oracle


class Departamento:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
        self.cursor = self.connection.cursor()

    def consultaBaseDatos(self, consulta, parametros = ()):

        try:
            self.cursor.execute(consulta, parametros)
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        contador = self.cursor.rowcount
        return self.cursor, contador

    """
    def lectura_departamento(self):
        cursor = self.connection.cursor()
        try:
            consulta = ("SELECT * FROM dept order by dept_no")
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def lectura_1_departamento(self, codigo):
        cursor = self.connection.cursor()
        try:
            consulta = ("SELECT * FROM dept where dept_no=:param1")
            cursor.execute(consulta, (codigo,))

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def insertar_departamento(self, numero, nombre, localidad):
        cursor = self.connection.cursor()
        try:
            consulta = ("INSERT INTO dept (dept_no,dnombre,loc) VALUES (:P1, :P2, :P3)")

            cursor.execute(consulta, (numero, nombre, localidad))

            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        contador = cursor.rowcount
        return cursor, contador
    
    def borrar_departamento(self, codigo):
        cursor = self.connection.cursor()
        try:
            consulta = ("Delete from dept where dept_no=:param1")

            cursor.execute(consulta, (codigo,))

            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor
    
    def modificar_departamento(self, localidad, codigo):
        cursor = self.connection.cursor()
        try:
            consulta = ("Update dept set loc=:Param1 where dept_no=:Param2")

            cursor.execute(consulta, (localidad,codigo))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor
    """
