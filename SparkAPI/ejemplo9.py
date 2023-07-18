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

# Visualizar el número de empleados por oficio. Usaremos un groupby
empleados.groupBy ("oficio"). count ().show ()
# Visualizar la media salarial por oficio. Usaremos un groupby
empleados.groupBy("oficio").avg ("salario").show ()