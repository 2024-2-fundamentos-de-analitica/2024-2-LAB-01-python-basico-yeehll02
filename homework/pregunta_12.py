"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput
import glob

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    # Leer archivo
    sequence = []
    files = glob.glob("files/input/data.csv")
    with fileinput.input(files=files) as f:
        for line in f:
            sequence.append((fileinput.filename(), line.strip()))
    
    resultado = {}
    for _, value in sequence:
        columna = value.split("\t")
        clave = columna[0]
        valores = columna[4].split(",")
        suma = 0
        for item in valores:
            key, value = item.split(":")
            suma+=int(value)
        if clave not in resultado.keys():
            resultado[clave] = 0
        resultado[clave] += suma
    resultado2 = {}
    for i in sorted(resultado.keys()):
        resultado2[i] = resultado[i]

    return resultado2
# print(pregunta_12())/