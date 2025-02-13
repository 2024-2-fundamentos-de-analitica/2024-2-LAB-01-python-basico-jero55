"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv", 'r') as file:
        data = file.readlines()
    maximo = {}
    minimo = {}
    for line in data:
        line = line.strip().split("	")
        if line[0] in maximo:
            if int(line[1]) > maximo[line[0]]:
                maximo[line[0]] = int(line[1])
        else:
            maximo[line[0]] = int(line[1])
        if line[0] in minimo:
            if int(line[1]) < minimo[line[0]]:
                minimo[line[0]] = int(line[1])
        else:
            minimo[line[0]] = int(line[1])
    
    salida = [(k, maximo[k], minimo[k]) for k in maximo.keys()]
    salida.sort()
    return salida