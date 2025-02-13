"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    with open("files/input/data.csv", 'r') as file:
        data = file.readlines()
    
    dic = {}
    for line in data:
        line = line.strip().split("	")
        letters = line[3].split(",")
        for letter in letters:
            if letter in dic:
                dic[letter] += int(line[1])
            else:
                dic[letter] = int(line[1])

    salida  = dict(sorted(dic.items()))

    return salida
