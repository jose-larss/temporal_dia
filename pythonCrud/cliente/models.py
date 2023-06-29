from django.db import models

from django.db import models

import cx_Oracle


class Cliente:
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
