"""
import pandas as pd

datos = {
    'nombre' : ['juan', 'maria', 'pedro', 'ana'],
    'edad' : [25, 30, 35, 38],
    'ciudad': ['madrid', 'barcelona', 'sevilla', 'cuenca']
}

df = pd.DataFrame(datos)
print(df)

for i in range(len(df)):
    print(df.iloc[i]['Nombre'])

"""

import pandas as pd

# Crear un DataFrame a partir de un diccionario
datos = {'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
         'Edad': [25, 30, 35, 28],
         'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']}

print('\n*** DATA FRAME ORIGINAL ***')
df = pd.DataFrame(datos)
print(df)


print('\n*** DATA FRAME df[\'Ciudad_Mayusculas\'] ***')
df['Ciudad_Mayusculas'] = df['Ciudad'].apply(lambda x: x.upper())

df['nuevo'] = df['Edad'].apply(lambda x: x > 10)

print(df)