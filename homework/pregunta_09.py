"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput
import glob


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    # Leer archivo
    sequence = []
    files = glob.glob("files/input/data.csv")
    with fileinput.input(files=files) as f:
        for line in f:
            sequence.append((fileinput.filename(), line.strip()))
    
    diccionario = {}
    for _, value in sequence:
        columna = value.split("\t")
        valores = columna[4].split(",")
        for item in valores:
            key, value = item.split(":")
            if key not in diccionario.keys():
                diccionario[key] = 0
            diccionario[key]+=1
    resultado={}
    for i in sorted(diccionario.keys()):
        resultado[i]=diccionario[i]
    return resultado
        

# print(pregunta_09())

