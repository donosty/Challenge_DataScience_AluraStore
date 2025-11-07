import pandas as pd

url1 = '~/Descargas/CursoPython/Pandas/challenge/BD/tienda_1.csv'
url2 = '~/Descargas/CursoPython/Pandas/challenge/BD/tienda_2.csv'
url3 = '~/Descargas/CursoPython/Pandas/challenge/BD/tienda_3.csv'
url4 = '~/Descargas/CursoPython/Pandas/challenge/BD/tienda_4.csv'


tienda1 = pd.read_csv(url1)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

print(tienda1.columns)
print()
print(tienda1.info())
#Ingreso total por cada tienda

ingreso_tienda1 = sum(tienda1['Precio'])
ingreso_tienda2 = sum(tienda2['Precio'])
ingreso_tienda3 = sum(tienda3['Precio'])
ingreso_tienda4 = sum(tienda4['Precio'])

#Ventas por categoria
print()

venta_tienda1 = tienda1.groupby('Categoría del Producto')['Producto'].count().sort_values(ascending=False)
venta_tienda2 = tienda2.groupby('Categoría del Producto')['Producto'].count().sort_values(ascending=False)
venta_tienda3 = tienda3.groupby('Categoría del Producto')['Producto'].count().sort_values(ascending=False)
venta_tienda4 = tienda4.groupby('Categoría del Producto')['Producto'].count().sort_values(ascending=False)

#Valoracion media por tienda
print()

calificacion_media_tienda1 = round(tienda1['Calificación'].mean(), 2)
calificacion_media_tienda2 = round(tienda2['Calificación'].mean(), 2)
calificacion_media_tienda3 = round(tienda3['Calificación'].mean(), 2)
calificacion_media_tienda4 = round(tienda4['Calificación'].mean(), 2)

#Productos mas vendidos y menos vendidos
