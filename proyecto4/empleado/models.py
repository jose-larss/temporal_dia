from django.db import models
import cx_Oracle

class Empleado:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
        self.cursor = self.connection.cursor()
        self.cursor2 = self.connection.cursor()
    def devolverdato(self,miOficio):

        try:
            consulta = ("SELECT apellido,oficio, salario FROM emp where UPPER(oficio)=UPPER(:p1)")
            consulta_contador = ("SELECT count(*) FROM emp where UPPER(oficio)=UPPER(:p1)")
            self.cursor.execute(consulta, (miOficio,))
            self.cursor2.execute(consulta_contador, (miOficio, ))

        except self.connection.Error as error:
            print("Error: ", error)

        return self.cursor