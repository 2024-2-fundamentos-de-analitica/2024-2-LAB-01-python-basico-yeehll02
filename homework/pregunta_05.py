"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput
import glob
import string
from itertools import groupby


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    # Leer archivo
    sequence = []
    files = glob.glob("files/input/data.csv")
    with fileinput.input(files=files) as f:
        for line in f:
            sequence.append((fileinput.filename(), line.strip()))

    #  Preprocesar el arhivo
    sequence = [
        (key, value.translate(str.maketrans("", "", string.punctuation)).strip())
        for key, value in sequence
    ]

    # Mapper
    result = []
    for _, value in sequence:
        columna = value.split("\t")
        result.append( (columna[0], int(columna[1])) ) 

    # Ordenarlo alfabeticamente
    result = sorted(result, key=lambda x: x[0])

    result2 = []
    for key, group in groupby(result, key=lambda x: x[0]):
        # print(list(group))
        values = [val for _, val in group]  
        result2.append((key, max(values), min(values)))
    return result2

# print(pregunta_05())