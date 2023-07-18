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

# Recuperamos los datos de todos los empleados que cumplan la condición del IN(isin)

empleados[empleados.oficio.isin("DIRECTOR","ANALISTA")].show()
empleados.select("apellido","oficio","salario")[empleados.oficio.isin("DIRECTOR","ANALISTA")].show ()