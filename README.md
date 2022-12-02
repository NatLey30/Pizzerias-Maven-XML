# Pizzerias-Maven-XML
Repositorio en el que se limpian los datos de los dataframes orders.csv y order_details.csv, para realizar un predicción de los ingredientes a comprar para la siguiente semana, para lo cual cogemos la última semana del dataset y miramos cuantos ingredientes hacen falta.

Por otro lado, también se realiza un análisis de datos en los 5 archvios dados (pero de los dos limpiados y formateados, se coge la versión 'ordenada'), en el que se obvserva cuantos nans y nulls hay, y de que tipo son cada columna.

Los ficheros de entrada son:
- orders.csv
- order_details.csv
- pizza_types.csv
- pizzas.csv
- data_dictionary.csv

Los ficheros de salida son:
- order_details_ordenado.csv
- orders_ordenado.csv
- compra_semanal.csv
- compra_semanal.xml
- analisis_datos.xml

Los archivos de transformación son:
- compra.py
- limpiar_datos.py
- analisis_datos_xml.py
