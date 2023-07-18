import pandas as pd
import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
#cursor = connection.cursor()

consulta = "select * from emp"

dataframe = pd.read_sql_query(consulta, connection)
#print(dataframe)
dataframe.to_excel("emp.xlsx", index=False)

"""
import cx_Oracle
import pandas as pd

conexion = cx_Oracle.connect("system", "javaoracle", "localhost/XE")

df = pd.read_sql_query('SELECT * FROM emp', conexion)

print('*** DATA FRAME EMP ***')
print(df)

df.to_excel('Emp.xlsx', index=False)
"""



