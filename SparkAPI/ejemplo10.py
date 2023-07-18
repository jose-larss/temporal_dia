import findspark
findspark.init()
#from pyspark import SparkContext
#from pyspark.sql import SQLContext
from pyspark.sql import SparkSession

sqlc  = SparkSession.builder.getOrCreate()
print(sqlc)
#sc = SparkContext('local', 'Spark SQL')
#sqlc = SQLContext(sc)
empleados = sqlc.read.json("C:\\APACHESPARK\\empleados.json")
#print(empleados['comision'])
#for i in range (len(empleados)):
#    print(empleados[i])

empleados.show()

empleados.printSchema()

#empleados.filter(empleados['oficio'] == "ANALISTA").show()
#empleados.filter(empleados['oficio'] != "ANALISTA").show()
empleados.filter(empleados['salario'] >= 350000).show()


