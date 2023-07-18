import findspark
findspark.init()
#from pyspark import SparkContext
#from pyspark.sql import SQLContext
from pyspark.sql import SparkSession

sqlc  = SparkSession.builder.getOrCreate()
#sc = SparkContext('local', 'Spark SQL')
#sqlc = SQLContext(sc)
empleados = sqlc.read.json("C:\\APACHESPARK\\empleados.json")

#sc = SparkContext('local', 'Spark SQL')
#sqlc = SQLContext(sc)

# Imprimimos todos los datos
#empleados.show()

# Pintamos el Schema para ver la información de los campos

#empleados.printSchema()

# Recuperamos el apellido,oficio,salario y comision de todos los registros
empleados.select("apellido","oficio","salario","comision").show()