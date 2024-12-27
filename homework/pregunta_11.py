"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput
import glob

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


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
        valor = columna[1]
        letras = columna[3].split(",")

        for letra in letras:
            if letra not in resultado.keys():
                resultado[letra] = 0
            resultado[letra] += int(valor)
        
    resultado2 = {}
    for i in sorted(resultado.keys()):
        resultado2[i] = resultado[i]
    return resultado2
# print(pregunta_11())
