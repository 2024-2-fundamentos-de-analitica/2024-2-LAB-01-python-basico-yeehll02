"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput
import glob

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    
    sequence = []
    files = glob.glob("files/input/data.csv")
    with fileinput.input(files=files) as f:
        for line in f:
            sequence.append((fileinput.filename(), line.strip()))
    # print(sequence)

    suma=0
    for i, line in sequence:
  
      columna= line.split("\t")
      print(columna)  
      suma+= int(columna[1])
      
    return suma

# print(pregunta_01())

