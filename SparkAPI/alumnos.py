
import pandas as pd

dataframe = pd.read_csv('alumnos.csv', delimiter=';')
print(dataframe)

dataframe.to_excel("alumnos.xlsx", index=False)
