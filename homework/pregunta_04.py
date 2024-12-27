"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import fileinput
import glob
import string

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

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
        fecha = value.split("\t")[2]
        m=fecha[4:6]
        result.append( (m, 1) ) 
   
    # Ordenarlo alfabeticamente
    result = sorted(result, key=lambda x: x[0])
    
    result2 = {}
    for key, value in result:
        if key not in result2.keys():
            result2[key] = 0
        result2[key] += value
    return list(result2.items())
    


# print(pregunta_04())
