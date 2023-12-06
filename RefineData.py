import pandas as pd
import numpy as np

def datos_refinados():
    df = pd.read_csv('datos_climaticos.csv', header=None)
    # Se reemplazan los headers por sus nombres
    headers = df.iloc[1]
    df.columns = headers

    # Se reemplazan los - con nulo
    df.replace("-", np.nan, inplace=True)

    # Se eliminan las columnas que no son necesarias
    df = df[['Año', 'Mes', 'Día', 'T', 'H', 'PP']]

    # Se convierten todas las columnas a valores numéricos y se reemplazan los no numéricos con NaN
    df = df.apply(pd.to_numeric, errors='coerce')

    # Se eliminan las filas con datos nulos
    df = df.dropna()

    # Se binariza la columna 'PP'
    df['PP'] = df['PP'].apply(lambda x: 1 if x > 0 else 0)

    # Se crea el futuro dataset para la red neuronal
    dataset = df[['Mes', 'T', 'H', 'PP']]
    dataset = dataset.sort_values(by='Mes')
    print(dataset.head())

    df.to_csv('datos_refinados.csv', index=False, header=True)
    dataset.to_csv('dataset.csv', index=False, header=True)