import pandas as pd


# Crear un DataFrame a partir de un diccionario
datos = {'Nombre': ['Benito', 'Andrea', 'Floro', 'María'],
         'Edad': [25, 30, 35, 45],
         'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']}



df = pd.DataFrame(datos)

# Mostrar el DataFrame
print('\n*** DATA FRAME ***')
#print(df)
for item in df:
    print(item)
    for i in item:
        print(i)

"""
# Filtrar filas basado en una condición
print('\n*** DATA FRAME FILTRADO ***')
df_filtrado = df[df['Edad'] > 30]

print(df_filtrado)

# Ordenar el DataFrame por una columna
print('\n*** DATA FRAME ORDENADO POR EDAD ***')
df_ordenado = df.sort_values('Edad')
print(df_ordenado)
"""
