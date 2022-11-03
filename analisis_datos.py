import pandas as pd
import xml.etree.ElementTree as ET


if __name__ == "__main__":

    ficheros_analizar = ['order_details.csv', 'orders.csv', 'data_dictionary.csv', 'pizzas.csv', 'pizza_types.csv']
    root = ET.Element('Análisis de NaN, null y tipologias')

    for fichero in ficheros_analizar:

        df = pd.read_csv(fichero, sep = ',', encoding = 'LATIN1')
        fichero = ET.SubElement(root, 'fichero', {'nombre': fichero})

        nans = str(df.isna().sum().sum())
        NaN = ET.SubElement(fichero, 'NaN_en_todo_el fichero', {'NaN': nans})

        nulls = str(df.isnull().sum().sum())
        Null = ET.SubElement(fichero, 'Null_en_todo_el_fichero', {'Null': nulls})

        columnas = df.columns.values
        for colum in range(len(columnas)):

            nombre = columnas[colum]
            columna = ET.SubElement(fichero, 'columna', {'nombre': nombre})

            tipo_col = str(df[columnas[colum]].dtype)
            tipo_columna = ET.SubElement(columna, 'tipo_dato', {'tipo': tipo_col})

    # escribimos en el xml
    tree = ET.ElementTree(root)
    tree.write('Analisis_datos.xml', xml_declaration=True, encoding='utf-8')