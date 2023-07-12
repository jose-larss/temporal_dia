import findspark
findspark.init()
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession

#sc = SparkContext('local', 'Spark SQL')
#sqlc = SQLContext(sc)
sqlc = SparkSession.builder.getOrCreate()
empleados = sqlc.read.json("C:\\APACHESPARK\\empleados.json")

# PASO MUY IMPORTANTE: Generamos una tabla llamada EMP con los datos del JSON.
# Al generar la tabla podemos realizar consultas SQL.

empleados.createOrReplaceTempView("EMP")

# Realizamos  consulta SQL

#empleadosConsulta = sqlc.sql("SELECT * FROM EMP where upper(APELLIDO) LIKE 'A%'")
empleadosConsulta = sqlc.sql("SELECT apellido, nvl(comision,0) as comisiones FROM EMP")


empleadosConsulta.show()