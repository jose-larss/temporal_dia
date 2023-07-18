
import pandas as pd


# Crear un DataFrame a partir de un diccionario
datos0 = {'Nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Luis', 'Laura', 'Miguel', 'Sara', 'Carlos', 'Lucía'],
         'Edad': [25, 30, 35, 28, 32, 27, 31, 29, 33, 26],
         'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Málaga', 'Bilbao', 'Alicante', 'Granada', 'Murcia', 'Zaragoza']}

df = pd.DataFrame(datos0)

# Mostrar el DataFrame
print('\n*** DATA FRAME ***')
print(df)

# recorrer dataframe por filas y columnas
for i in range(len(df)):
    print(df.iloc[i]['Nombre'])


# Agrupar y resumir datos
print('\n*** DATA FRAME AGRUPAR Y RESUMIR ***')
df_agrupado = df['Edad'].mean()
print('Media de edad:', df_agrupado)