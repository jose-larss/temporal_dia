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
dp = sqlc.read.json("C:\\APACHESPARK\\departamentos.json")
dp.createOrReplaceTempView("DEPT")


# Realizamos  consulta SQL

empleadosConsulta = sqlc.sql("SELECT apellido,loc FROM EMP inner join DEPT on EMP.dept_no=DEPT.dept_no")

empleadosConsulta.show()