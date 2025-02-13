"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    with open("files/input/data.csv", mode='r') as file:
        data = file.readlines()

    suma = {}

    for line in data:
        line = line.strip().split("	")
        
        if line[0] in suma:
            suma[line[0]] += int(line[1])
        else:
            suma[line[0]] = int(line[1])

    salida = [(k, v) for k, v in suma.items()]

    salida.sort()
    
    return salida        