def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Establecer una bandera para verificar si se realizan intercambios en esta pasada
        swapped = False
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                # Realizar el intercambio de elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Establecer la bandera en True para indicar que se realizó un intercambio
                swapped = True
        # Si no se realizaron intercambios en esta pasada, el arreglo ya está ordenado
        if not swapped:
            break
    return arr


# Definir el arreglo a ordenar
arr = [2, 9, 5, 8, 12, 4, 7, 25]

# Llamar a la función de ordenamiento de burbuja
sorted_arr = bubble_sort(arr)

# Imprimir el arreglo ordenado
print(sorted_arr)
