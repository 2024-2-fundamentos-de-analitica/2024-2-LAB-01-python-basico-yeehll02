"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import fileinput
import glob
import string

def pregunta_02():

    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

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
        result.append( (columna[0], 1) ) 

    # Ordenarlo alfabeticamente
    result = sorted(result, key=lambda x: x[0])
    
    result2 = {}
    for key, value in result:
        if key not in result2.keys():
            result2[key] = 0
        result2[key] += value
    return list(result2.items())
    


# print(pregunta_02())
