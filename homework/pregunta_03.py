"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput
import glob
import string

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

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
    
    result2 = {}
    for key, value in result:
        if key not in result2.keys():
            result2[key] = 0
        result2[key] += value
    return list(result2.items())

# print(pregunta_03())