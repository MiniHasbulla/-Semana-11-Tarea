def quicksort(arr, low, high):

    if low < high:
        #Encuentra el índice
        pi = partition(arr, low, high)
        #Ordena
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def ordenar_fila(matriz, fila_index):

    if 0 <= fila_index < len(matriz):
        quicksort(matriz[fila_index], 0, len(matriz[fila_index]) - 1)
    else:
        print(f"Índice de fila {fila_index} fuera de rango.")


def imprimir_matriz(matriz, mensaje):

    if mensaje:
        print(mensaje)
    for fila in matriz:
        print(fila)


#Matriz
matriz = [
    [10, 3, 5, 1],
    [4, 9, 2, 8],
    [7, 6, 12, 11],
    [15, 14, 13, 16]
]

#Índice de la fila
fila_a_ordenar = 1

#Imprimir
imprimir_matriz(matriz, "Matriz original:")

#Ordenar
ordenar_fila(matriz, fila_a_ordenar)

#Imprimir la fila ordenada
imprimir_matriz(matriz, "Matriz después de ordenar la fila 1:")
