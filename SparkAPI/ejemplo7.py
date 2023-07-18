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


# Recuperamos el apellido y oficio de los empleados que su primera letra del apellido sea una 's'
empleados.select ("apellido", "oficio")[empleados.apellido.startswith ("s")].show()
# Recuperamos el apellido y oficio de los empleados que su última letra del apellido sea una 'o'
empleados.select ("apellido", "oficio")[empleados.apellido.endswith("o")].show()