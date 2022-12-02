import pandas as pd
import xml.etree.ElementTree as ET


def archivo(fichero):
    '''
    Función que va a analizar cada archivo buscando cuantos
    Nans y Nulls hay en todo el csv. También va a estudiar la
    tipología de cada columna, a la vaz que mira cuantos
    Nans y Nulls hay en esta.
    '''
    df = pd.read_csv(fichero, sep = ',', encoding = 'LATIN1')
    fichero = ET.SubElement(root, 'fichero', {'nombre': fichero})

    # Nans totales
    nans = str(df.isna().sum().sum())
    ET.SubElement(fichero, 'NaN_en_todo_el_fichero', {'nº': nans})

    # Nulls totales
    nulls = str(df.isnull().sum().sum())
    ET.SubElement(fichero, 'Null_en_todo_el_fichero', {'nº': nulls})

    # Sacamos columnas
    columnas = df.columns.values

    # Para cada columna
    for colum in range(len(columnas)):
        nombre = columnas[colum]
        columna = ET.SubElement(fichero, 'columna', {'nombre': nombre})

        # Buscamos su tipología
        tipo_col = str(df[columnas[colum]].dtype)
        ET.SubElement(columna, 'tipo_dato', {'tipo': tipo_col})

        # Número de nans
        nans_col = str(df[columnas[colum]].isna().sum().sum())
        ET.SubElement(columna, 'nans_columna', {'nº': nans_col})

        # Número de nulls
        nulls_col = str(df[columnas[colum]].isnull().sum().sum())
        ET.SubElement(columna, 'nulls_columna', {'nº': nulls_col})


if __name__ == "__main__":

    root = ET.Element('Análisis')

    fichero = archivo('order_details_ordenado.csv')
    fichero = archivo('orders_ordenado.csv')
    fichero = archivo('data_dictionary.csv')
    fichero = archivo('pizzas.csv')
    fichero = archivo('pizza_types.csv')

    # Escribimos en el xml
    tree = ET.ElementTree(root)
    ET.indent(tree)
    tree.write('analisis_datos.xml', xml_declaration=True, encoding='utf-8')
