import findspark
findspark.init()
#from pyspark import SparkContext
#from pyspark.sql import SQLContext
from pyspark.sql import SparkSession

#sc = SparkContext('local', 'Spark SQL')
#sqlc = SQLContext(sc)
sqlc  = SparkSession.builder.getOrCreate()
empleados = sqlc.read.json("C:\\APACHESPARK\\empleados.json")

# Imprimimos todos los datos
empleados.show()

# Pintamos el Schema para ver la información de los campos

empleados.printSchema()
