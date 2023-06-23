from django.db import models

import cx_Oracle


class Departamento:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def lectura_departamento(self):
        cursor = self.connection.cursor()
        try:
            consulta = ("SELECT * FROM dept order by dept_no")
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def insertar_departamento(self, numero, nombre, localidad):
        cursor = self.connection.cursor()
        try:
            consulta = ("INSERT INTO dept (dept_no,dnombre,loc) VALUES (:P1, :P2, :P3)")

            cursor.execute(consulta, (numero, nombre, localidad))
            #contador = cursor.rowcount

            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

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
