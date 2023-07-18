import pandas as pd

# Cargar datos desde un archivo CSV
df = pd.read_csv('datos.csv', delimiter=';')


# Mostrar el DataFrame
#print('\n*** DATA FRAME ***')
#print(df)

#print('\n*** PRIMERAS 10 FILAS ***')
#print(df.head(10))


#print('\n*** DICCIONARIO ***')
'''
Convertir el DataFrame en un diccionario de registros
Cada registro es un diccionario con:
* claves correspondientes a los nombres de las columnas
* valores correspondientes a los datos de cada fila.
'''
diccionario = df.to_dict(orient='records')



for registro in diccionario:
    print(registro)
