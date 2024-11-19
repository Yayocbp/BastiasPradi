import pandas as pd
import re #importa el modulo para expresiones regulares


#2.1 Lectura y analisis exploratorio de datos

df = pd.read_csv('ejemplo_data.csv')
print(df)
print()#Linea en blanco
print("Tipos de variables en cada Columna")
print(df.dtypes)
print()

df['ID'] = df['ID'].fillna(0).astype(int)
df['ID']= df['ID'].astype(int)
print(df)
print()#Linea en blanco
print("Tipos de variables en cada Columna")
print(df.dtypes)
print()

df['Activo'] = df['Activo'].astype(bool)
print(df)
print()#Linea en blanco
print("Tipos de variables en cada Columna")
print(df.dtypes)
print()

df['Nombre'] = df['Nombre'].astype('category')
print(df)
print()#Linea en blanco
print("Tipos de variables en cada Columna")
print(df.dtypes)
print()

#Este codigo no puede cambiar directamente el atributo "2016 y 2017", ya que los datos son string
#df['2016'].astype('float')

#se crea una funcion para cambiar el tipo de dato

def convertir(val):
    nuevo_data = val.replace(',','').replace('$','').replace('%','')
    return float(nuevo_data)

df['2016'] =df['2016'].apply(convertir)
df['2017'] = df['2017'].apply(convertir)
df['Crecimiento']=df['Crecimiento'].apply(convertir)
print(df)
print()#Linea en blanco
print("Tipos de variables en cada Columna")
print(df.dtypes)
print()


#ejemplo de lo que no se puede hacer al convertir datos a enteros en forma directa, ya que algunos registros con string

#df['Unidades'].astype('int')}

#con este codigo modifico los valores de un campo y en el caso que no tenga valores numericos, los reemplaza por un 4 o el valor que quiera
df['Unidades'] = pd.to_numeric(df['Unidades'], errors= 'coerce').fillna(4)
df['Unidades']= df['Unidades'].astype(int)
print(df)
print()#Linea en blanco
print("Tipos de variables en cada Columna")
print(df.dtypes)
print()

#En el siguiente ejercicio lo que haremos es cambiar los valores del atributo fecha a fECHA

df['fecha']= pd.to_datetime(df['fecha'])
print(df)
print()#Linea en blanco
print("Tipos de variables en cada Columna")
print(df.dtypes)
print()

#2.2 Lectura y analisis exploratorio de datos 2

#Cargar el archivo de Nombre ecommerce.csv, se agrega encoding= latin1, debido a que no me abria el archivo, que posiblemente no estaba codificado en UTF-8
df = pd.read_csv('ecommerce_data.csv',encoding='latin1')
print(df)
print()
print('Tipos de variables en cada columna')
print(df.dtypes)
print()

#Utilizando la funcion astype transforme el atributo "InvoiceNo" a entero
#Filtrar filas con solo numeros en InvoiceNo
df = df[df['InvoiceNo'].str.isdigit()]
#Convertir la columna a int despues de eliminar valores no numericos
df['InvoiceNo'] = df['InvoiceNo'].astype(int)
print(df)
print()
print('Tipos de variables en cada columna')
print(df.dtypes)
print()

#Utilizando la funcion astype transforme el atributo "Description" a string.
df['Description'].fillna('', inplace=True)
df['Description'] = df['Description'].apply(lambda x: re.sub(r'[^A-Za-z0-9\s]', '', x))  # Mantén solo letras, números y espacios
df['Description'] = df['Description'].str.strip()  # Elimina espacios al inicio y al final
df['Description'] = df['Description'].str.replace(r'\s+', ' ', regex=True)  # Sustituye múltiples espacios por uno solo
df['Description'] = df['Description'].str.lower()  # Convierte a minúsculas (opcional)
df['Description'] = df['Description'].astype(str)
#print(df)
#print()
print('Tipos de variables en cada columna')
print(df.dtypes)
print()


#Convierta el atributo "Quantity" a entero
df['Quantity'] = df['Quantity'].astype(int)
print(df)
print()
print('Tipos de variables en cada columna')
print(df.dtypes)
print()

#Convierta el atributo "UnitPrice" a Float
df['UnitPrice'] = df['UnitPrice'].astype(float)
print(df)
print()
print('Tipos de variables en cada columna')
print(df.dtypes)
print()

#La columna "InvoiceDate" contiene un string que representa "fecha-hora", separe la columna en
#dos columnas que representen cada atributo por separado.
# Separar la columna 'InvoiceDate' en 'Fecha' y 'Hora'
df[['Fecha', 'Hora']] = df['InvoiceDate'].str.split(' ', expand=True)
print(df)
print()
print('Tipos de variables en cada columna')
print(df.dtypes)
print()

#Anada una nueva columna que represente el monto total para cada boleta.
# Crear la columna 'Total_Boleta' multiplicando 'UnitPrice' por 'Quantity'
df['Total_Boleta'] = df['UnitPrice'] * df['Quantity']
print(df)
print()
print('Tipos de variables en cada columna')
print(df.dtypes)
print()

# Exportar el DataFrame a un archivo CSV, guardada por defecto en la carpeta Actividades

df.to_csv('Ecommer_nuevo.csv', index=False)

