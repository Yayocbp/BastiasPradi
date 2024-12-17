import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

# Paso 1: Cargar los datos
# Se carga el archivo CSV usando pandas. El archivo contiene dos columnas: A y B.
# Cargar el archivo CSV
data = pd.read_csv('kmeans.1.csv') 
print(data.head())
print()

# Paso 2: Visualizar los datos originales
# Creamos un gráfico de dispersión para observar la relación entre las variables A y B.
plt.figure(figsize=(8, 6))
plt.scatter(data['A'], data['B'], c='blue', alpha=0.5, label='Datos Originales')
plt.title('Gráfico de Dispersión de Variables A y B')
plt.xlabel('A')
plt.ylabel('B')
plt.legend()
plt.grid(True)
plt.show()

# Paso 3: Normalizar los datos
# La normalización ajusta los valores para que estén en el rango [0, 1].
# Esto es importante porque K-Means es sensible a las escalas de las variables.
scaler = MinMaxScaler()  # Usamos MinMaxScaler para la normalización.
data_norm = scaler.fit_transform(data[['A', 'B']])  # Normalizamos A y B.
data_norm = pd.DataFrame(data_norm, columns=['A', 'B'])  # Convertimos a DataFrame.

print("\nPrimeras filas de los datos normalizados:")
print(data_norm.head())

# Paso 4: Aplicar K-Means con 7 clusters como muestra
# K-Means agrupa los puntos en k clusters buscando minimizar la distancia intra-clases.
# k-means++' es un método mejorado que selecciona inicializaciones de centroides de manera 
# que minimice las posibilidades de converger a un mal resultado. Es más eficiente y estable que la inicialización aleatoria pura.
# n_init specifica cuántas veces se ejecutará el algoritmo completo con diferentes inicializaciones de centroides. Por defecto, el algoritmo
# elige la mejor solución (la que tiene la menor inercia o suma de distancias al cuadrado dentro de los clusters).
# max_iter=300, es el número máximo de iteraciones que el algoritmo realizará para intentar ajustar los clusters en 
# cada ejecución. Si se alcanzan las 300 iteraciones sin converger, el proceso se detendrá.
# random_state=42, Fija la semilla del generador de números aleatorios para que los resultados sean reproducibles. 
# Cambiar este número da lugar a diferentes inicializaciones y resultados, pero con el mismo número se obtendrán los mismos resultados al ejecutar el código varias veces
kmeans = KMeans(n_clusters=7, init='k-means++', n_init=15, max_iter=200, random_state=42) # se modifican los datos originales
kmeans.fit(data_norm)  # Ajustamos el modelo a los datos normalizados.

# Extraemos resultados importantes del modelo:
centroids = kmeans.cluster_centers_  # Coordenadas de los centroides de los clusters.
labels = kmeans.labels_  # Etiqueta (cluster) asignada a cada punto.
inertia = kmeans.inertia_  # Distancia intra-clases total.
print("\nResultados de K-Means con 7 clusters:")
print("Centroides:\n", pd.DataFrame(centroids, columns=['A', 'B']))
#data_norm ['labels'] = labels
print(data_norm.head())
print("Primeras 10 etiquetas asignadas:", labels[:10])
print("Inercia Total (Distancia intra-clases):", inertia)

# Paso 5: Evaluar K-Means para diferentes números de clusters (k)
# Guardamos la inercia para diferentes valores de k en un diccionario.
inertia_dict = {}
for k in range(1, 8):  # Probamos con k=1 hasta 8
    #
    kmeans = KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=300, random_state=42)
    kmeans.fit(data_norm)
    # La inercia nos indica que tan pegados estan los registros a cada centroide, mientras más pegados esten al cluster, mejor se identifica, no necesariamente al aumentar el K,
    # se verifica el mismo resultado, puede pasar que un solo registro quede asociado a un cluster, las metricas siempre deban estar asociadas al contexto de los datos que estamos analizando
    # no hay que guiarse por una metrica que no este asociada al negocio, se dice que un buen modelo de clusterizado tiene un valor de K pequeño y un valor de inercia pequeño, lo que
    # no se da siempre. mayor importancia a los datgos que se encuentran mas lejos y menor importancia a valores que se encuentran mas cerca. lainersia suma todas las distancias y
    #las pondera que se tiene para un cluster dado.
    #
    inertia_dict[k] = kmeans.inertia_  # Guardamos la inercia para cada k.

print("\nInercia para diferentes valores de k:", inertia_dict)


# # Paso 6: Gráfico de clusters y centroides, aqui se puede visualizar claramente los centrum con su respectivos cluster, en este caso 7 cluster

# Paso 6: Gráfico de clusters y centroides
plt.figure(figsize=(8, 6))

# Visualizamos los puntos de cada cluster
for cluster in range(7):  # Número de clusters usados
    cluster_points = data_norm[labels == cluster]  # Seleccionamos puntos de este cluster
    plt.scatter(cluster_points['A'], cluster_points['B'], label=f'Cluster {cluster+1}', alpha=0.6)

# Graficamos los centroides
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=100, label='Centroides')
plt.title('Clusters y Centroides')
plt.xlabel('A (Normalizado)')
plt.ylabel('B (Normalizado)')
plt.legend()
plt.grid(True)
plt.show()

# Paso 7: Gráfico de la distancia intra-clases
# Graficamos la inercia en función del número de clusters.
plt.figure(figsize=(8, 6))
plt.plot(list(inertia_dict.keys()), list(inertia_dict.values()), marker='o', linestyle='-', color='blue')
plt.title('Distancia Intra-Clases vs Número de Clusters (k)')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('Distancia Intra-Clases (Inercia)')
plt.xticks([1, 2, 3, 4, 5])
plt.grid(True)
plt.show()

# Paso 8: Determinar el número óptimo de clusters usando el criterio del codo
# El codo se encuentra en el punto donde la disminución de la inercia se estabiliza, se  logra un buen balance entre simplicidad y calidad del agrupamiento, utilizamos
#un k=2, este no capturaria adecuadamente las diferencias en los datos.
optimal_k = 4  # En este caso, observamos que el codo está en k=4.
print("\nNúmero óptimo de clusters según el criterio del codo:", optimal_k)




