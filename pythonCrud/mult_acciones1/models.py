from django.db import models

import cx_Oracle

#Estas clases son las que ha usado el profesor con fetchall()
class Departamento:
    def __init__(self):
        self.connection = cx_Oracle.connect('system', 'pythonoracle', 'localhost/XE')

    def nombreshosp(self):
        cursor = self.connection.cursor()
        consulta = "SELECT NOMBRE, HOSPITAL_COD FROM HOSPITAL"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        return resultado

    def doctoreshosp(self, cod_hospital):
        datos = ', '.join(cod_hospital)
        cursor = self.connection.cursor()
        consulta = f"SELECT APELLIDO, ESPECIALIDAD, SALARIO FROM DOCTOR WHERE HOSPITAL_COD IN ({datos})"
        print(consulta)
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        return resultado

    def consultaBaseDatos(self, consulta, parametros = ()):
        self.cursor = self.connection.cursor()
        msj_error = ""
        try:
            self.cursor.execute(consulta, parametros)
            #El rowcount siempre tiene que ir entes del commit
            contador = self.cursor.rowcount
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)
            msj_error = f"Error {error}"

        return self.cursor, contador, msj_error
