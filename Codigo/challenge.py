import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url1 = '~/Descargas/CursoPython/Pandas/challenge/BD/tienda_1.csv'
url2 = '~/Descargas/CursoPython/Pandas/challenge/BD/tienda_2.csv'
url3 = '~/Descargas/CursoPython/Pandas/challenge/BD/tienda_3.csv'
url4 = '~/Descargas/CursoPython/Pandas/challenge/BD/tienda_4.csv'


tienda1 = pd.read_csv(url1)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

#Ingreso total por cada tienda

ingreso_tienda1 = sum(tienda1['Precio'])
ingreso_tienda2 = sum(tienda2['Precio'])
ingreso_tienda3 = sum(tienda3['Precio'])
ingreso_tienda4 = sum(tienda4['Precio'])

#Ventas por categoria

venta_tienda1 = tienda1.groupby('Categoría del Producto')['Producto'].count().sort_values(ascending=False)
venta_tienda2 = tienda2.groupby('Categoría del Producto')['Producto'].count().sort_values(ascending=False)
venta_tienda3 = tienda3.groupby('Categoría del Producto')['Producto'].count().sort_values(ascending=False)
venta_tienda4 = tienda4.groupby('Categoría del Producto')['Producto'].count().sort_values(ascending=False)

#Valoracion media por tienda

calificacion_media_tienda1 = round(tienda1['Calificación'].mean(), 2)
calificacion_media_tienda2 = round(tienda2['Calificación'].mean(), 2)
calificacion_media_tienda3 = round(tienda3['Calificación'].mean(), 2)
calificacion_media_tienda4 = round(tienda4['Calificación'].mean(), 2)

#Productos mas vendidos y menos vendidos

productos_tienda1 = tienda1.groupby('Producto')['Producto'].count().sort_values(ascending=False)
productos_tienda2 = tienda2.groupby('Producto')['Producto'].count().sort_values(ascending=False)
productos_tienda3 = tienda3.groupby('Producto')['Producto'].count().sort_values(ascending=False)
productos_tienda4 = tienda4.groupby('Producto')['Producto'].count().sort_values(ascending=False)

#Valor promedio de costo de envio

costo_envio_tienda1 = round(tienda1['Costo de envío'].mean(), 2)
costo_envio_tienda2 = round(tienda2['Costo de envío'].mean(), 2)
costo_envio_tienda3 = round(tienda3['Costo de envío'].mean(), 2)
costo_envio_tienda4 = round(tienda4['Costo de envío'].mean(), 2)


array_nombres = ['Tienda 1', 'Tienda 2', 'TIenda 3', 'TIenda 4']

#Grafico Ventas por Categoria (Solo tienda 1) - (Grafico de barras)
venta_tienda1.plot(kind='barh', figsize=(12,8), color='blue')
plt.title("Ventas por Categoria en Tienda 1")
plt.xlabel("Numero de ventas por Categoria")
plt.ylabel("Categoria")
plt.show()

#Grafico productos mas vendidos (Solo tienda 1 y 2) - (Grafico de sipersion)
mas_vendidos_df = pd.concat([productos_tienda1, productos_tienda2, productos_tienda3, productos_tienda4], axis=1)
mas_vendidos_df.columns = array_nombres

mas_vendidos_df.plot(kind='scatter', x='Tienda 1', y='Tienda 2', figsize=(15,10), color='purple')
plt.title('Relacion de ventas: Tienda 1 vs Tienda 2')
plt.xlabel('Tienda 1')
plt.ylabel('Tienda 2')
plt.grid(True)
plt.show()

#Grafico ingreso total por tienda (Grafico de pastel)
array_tiendas = ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4']
array_ingreso = [ingreso_tienda1, ingreso_tienda2, ingreso_tienda3, ingreso_tienda4]

plt.figure(figsize=(15, 10))
plt.pie(array_ingreso, labels=array_tiendas, autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Ingreso Total por Tienda')
plt.show()

#Grafico de calor para analisis del desempeño geofrafico
df_latitudes = pd.concat([tienda1['lat'],tienda2['lat'],tienda3['lat'],tienda4['lat']], axis=1)
df_latitudes.columns = array_nombres

latitudes = pd.concat([df_latitudes[col] for col in df_latitudes.columns], ignore_index=True)

df_longitudes = pd.concat([tienda1['lon'],tienda2['lon'],tienda3['lon'],tienda4['lon']], axis=1)
df_longitudes.columns = array_nombres

longitudes = pd.concat([df_longitudes[col] for col in df_longitudes.columns], ignore_index=True)

coordenadas = pd.DataFrame({
    'latitud':latitudes,
    'longitud':longitudes
})

coordenadas = coordenadas.dropna()
coordenadas = coordenadas.astype(float)

heatmap, xedges, yedges = np.histogram2d(
    coordenadas['longitud'],
    coordenadas['latitud'],
    bins=(50,50)
)

plt.figure(figsize=(15,10))
plt.imshow(
    heatmap.T,
    origin='lower',
    cmap='inferno',
    extent=[
        coordenadas['longitud'].min(),
        coordenadas['longitud'].max(),
        coordenadas['latitud'].min(),
        coordenadas['latitud'].max()
    ]
)

plt.title('Mapa de calor de la distribucion geografica de productos vendidos')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.colorbar(label='Densidad de Ventas')
plt.show()

"""

El propósito de este análisis es evaluar el rendimiento comercial y operativo de cuatro tiendas en línea con el fin de identificar patrones de venta, desempeño geográfico y diferencias en el comportamiento de los consumidores.
A través del uso de Python, Pandas y Matplotlib, se procesaron y visualizaron datos que incluyen precios, categorías de productos, calificaciones, costos de envío y coordenadas geográficas de cada venta.
El objetivo es obtener una visión clara sobre:

* Cuáles son las categorías más vendidas.
* Qué tiendas generan mayores ingresos.
* Cómo se distribuyen geográficamente las ventas.
* Qué relación existe entre las tiendas en términos de volumen de ventas.

Este tipo de análisis resulta clave para tomar decisiones estratégicas sobre marketing, logística y gestión de inventario.

Desarrollo y análisis de resultados

Análisis de ventas por categoría

Se utilizó un gráfico de barras horizontales para mostrar las categorías más vendidas en la Tienda 1.
El propósito de esta visualización es identificar los productos que concentran la mayor demanda, ayudando a optimizar inventarios y estrategias de promoción.

python
venta_tienda1.plot(kind='barh', figsize=(12,8), color='blue')
plt.title("Ventas por Categoria en Tienda 1")
plt.xlabel("Numero de ventas por Categoria")
plt.ylabel("Categoria")
plt.show()


Interpretación:
El gráfico evidencia cuáles son las categorías con mayor número de ventas, reflejando las preferencias del consumidor y posibles oportunidades de expansión o mejora en otras líneas de producto.



Relación de ventas entre tiendas

Mediante un gráfico de dispersión, se compararon los volúmenes de productos vendidos entre la Tienda 1 y la Tienda 2.

python
mas_vendidos_df.plot(kind='scatter', x='Tienda 1', y='Tienda 2', figsize=(15,10), color='purple')
plt.title('Relacion de ventas: Tienda 1 vs Tienda 2')
plt.xlabel('Tienda 1')
plt.ylabel('Tienda 2')
plt.grid(True)
plt.show()

Interpretación:
La dispersión de los puntos permite observar si existe correlación entre ambas tiendas. Una tendencia ascendente indicaría que los mismos productos tienden a tener éxito en ambas, lo que sugiere patrones de consumo similares.


Ingreso total por tienda

Se generó un gráfico de pastel para visualizar el porcentaje de ingresos de cada tienda respecto al total general.

python
plt.figure(figsize=(15, 10))
plt.pie(array_ingreso, labels=array_tiendas, autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Ingreso Total por Tienda')
plt.show()

Interpretación:
El gráfico muestra la proporción de ingresos generados por cada tienda, destacando cuáles contribuyen más al rendimiento total y permitiendo detectar aquellas con **mayor potencial económico** o **necesidad de mejora**.


Desempeño geográfico (Mapa de calor)

Para analizar la distribución espacial de las ventas, se elaboró un mapa de calor que refleja la concentración de transacciones según latitud y longitud.

python
plt.imshow(
    heatmap.T,
    origin='lower',
    cmap='inferno',
    extent=[
        coordenadas['longitud'].min(),
        coordenadas['longitud'].max(),
        coordenadas['latitud'].min(),
        coordenadas['latitud'].max()
    ]
)
plt.colorbar(label='Densidad de Ventas')
plt.show()

Interpretación:
Las zonas con mayor intensidad cromática representan áreas con alta concentración de ventas, lo que puede indicar regiones con mayor demanda o mejor alcance logístico. Este análisis es útil para decisiones de expansión geográfica** o **optimización de distribución.

Dicho esto, la tienda numero 4 deberia de ser la vendida, gracias a este analisis se descubrio que es la tienda que menos ganancias, esta por debajo de la tienda 2 y 3 en cuanto a la calificacion y solo supera a la tienda 1 por 2 decimas, en el costo de envio promedio aunque no es el mas costoso, es menor por la cantidad de ventas y ganancias que está dejando esta tienda

"""