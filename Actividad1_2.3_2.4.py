import pandas as pd
import numpy as np

# Crear el diccionario con 50 valores
registros = {
    'ID': [i for i in range(50)],                    # ID desde 0 hasta 49
    'Edad': np.random.randint(18, 30, 50).tolist(),  # 50 edades aleatorias entre 18 y 30
    'normal': [round(np.random.normal(0, 1), 2) for _ in range(50)],  # 50 valores con distribución normal redondeados
    'Nota': [round(np.random.uniform(1.0, 7.0), 2) for _ in range(50)] # 50 notas aleatorias redondeadas
}

# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(registros)

# Mostrar el DataFrame
print("Data Frame solicitado, se muestran solo los 15 primeros registros")
print(df.head(15))
print()

#Obtener estadistica descriptiva de tendencia central

#Media

# Calcular la media de la columna 'Edad'
media_edad = df['Edad'].mean()

# Imprimir la media
print()
print("Cálculo de Media de la Edad:", media_edad)

print()

# Calcular la moda de la columna 'Edad'
moda_edad = df['Edad'].mode()

# Imprimir la moda con un mensaje
print("Cálculo de la Moda de la columna 'Edad':", moda_edad.tolist())
print()
#Agregue la columna Peso a df
df['Peso'] = np.random.randint(50, 70, len(df))
print(df.head(10))#muestro solo 10 registros
print()
# Calcular el promedio ponderado entre 'Edad' y 'Peso'
promedio_ponderado = (df['Edad'] * df['Peso']).sum() / df['Peso'].sum()

# Imprimir el resultado
print("Promedio ponderado entre Edad y Peso:", round(promedio_ponderado, 2))
print()
# Calcular la mediana de la columna 'Nota'
mediana_nota = df['Nota'].median()

# Imprimir el resultado
print("Mediana de la columna 'Nota':",round(mediana_nota),2)

#Calculo de Rango de Edad y Nota

rango_edad= df['Edad'].max() - df['Edad'].min()
rango_nota= df['Nota'].max() - df['Nota'].min()
print()
#Resultados
print("Rango de la columna 'Edad':", rango_edad)
print("Rango de la columna 'Nota':", rango_nota)

#Obtenga Estadisticas Descriptivas de dispersion

#Calculo de la Varianza del Peso, de la Nota y de la Edad

varianza_peso = df['Peso'].var()
varianza_nota = df['Nota'].var()
varianza_edad = df['Edad'].var()
print()
print("Varianza de la columna 'Peso':", round(varianza_peso, 2))
print("Varianza de la columna 'Nota':", round(varianza_nota, 2))
print("Varianza de la columna 'Peso':", round(varianza_edad, 2))

