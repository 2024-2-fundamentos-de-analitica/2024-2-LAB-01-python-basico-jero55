"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    with open("files/input/data.csv", mode='r') as file:
        data = file.readlines()

    contador = {}
    for linea in data:
        linea = linea.strip().split("	")
        letra = linea[0]
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1

    lista = [(k, v) for k, v in contador.items()]

    lista.sort()

    return lista