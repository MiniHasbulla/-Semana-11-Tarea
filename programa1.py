#Definición
matriz = [
    [14, 26, 322, 4123],
    [54, 633, 70, 81],
    [9131, 1023, 1144, 1652],
    [19, 11, 5, 165]
]


def buscar_valor(matriz, valor):

    for i, fila in enumerate(matriz):
        for j, elemento in enumerate(fila):
            if elemento == valor:
                return (True, i, j)
    return (False, -1, -1)

valor_a_buscar = 11

#Búsqueda
encontrado, fila, columna = buscar_valor(matriz, valor_a_buscar)

#Resultados
if encontrado:
    print(f"El valor {valor_a_buscar} se encontró en la posición ({fila}, {columna})")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
