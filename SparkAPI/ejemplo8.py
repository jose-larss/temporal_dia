import findspark
findspark.init()
#from pyspark import SparkContext
#from pyspark.sql import SQLContext
from pyspark.sql import SparkSession

sqlc  = SparkSession.builder.getOrCreate()
#sc = SparkContext('local', 'Spark SQL')
#sqlc = SQLContext(sc)
empleados = sqlc.read.json("C:\\APACHESPARK\\empleados.json")

# Imprimimos todos los datos
empleados.show()

# Pintamos el Schema para ver la información de los campos

empleados.printSchema()

# Mostrar las tres primeras letras del apellido de los empleados
empleados.select (empleados.apellido.substr(1, 3)).show()

# Mostrar las tres primeras letras del apellido de los empleados y dar un alias a la columna
empleados.select (empleados.apellido.substr(1, 3).alias ("Iniciales")).show()
