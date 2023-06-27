from django.db import models

import cx_Oracle


class Departamento:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def lectura_departamento(self, consulta, param=()):

        cursor = self.connection.cursor()
        try:
            cursor.execute(consulta, param)
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        contador = cursor.rowcount

        return cursor, contador
    
    def lectura_departamento_fetch(self, consulta, param=()):

        cursor = self.connection.cursor()
        try:
            cursor.execute(consulta, param)
            self.connection.commit()
            resultado = cursor.fetchall()

        except self.connection.Error as error:
            print("Error: ", error)

        return resultado
    
    """
    def lectura_1_registro(self, id_dept):
        cursor = self.connection.cursor()
        try:
            consulta = ("SELECT * FROM dept where dept_no=:param1")
            cursor.execute(consulta, (id_dept, ))

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor
    """
    """
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
    """
    """
    def borrar_departamento(self, codigo):
        cursor = self.connection.cursor()
        try:
            consulta = ("Delete from dept where dept_no=:param1")

            cursor.execute(consulta, (codigo,))

            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor
    """
    """
    def modificar_departamento(self, localidad, nombre,codigo):
        cursor = self.connection.cursor()
        try:
            consulta = ("Update dept set loc=:Param1, dnombre=:Param2  where dept_no=:Param3")

            cursor.execute(consulta, (localidad,nombre,codigo))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor
    """
