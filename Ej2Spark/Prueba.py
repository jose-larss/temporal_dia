import findspark
findspark.init()
from pyspark import SparkContext
sc=SparkContext(master="local",appName="Spark demo")
print(sc.textFile("c:\\Prueba.txt").first())