# Example 1
def calculate_area(radius):
    pi = 3.14159
    return pi * radius * radius

def calculate_area(radius):
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
    radius (float): El radio del círculo.

    Retorna:
    float: El área del círculo.
    """
    pi = 3.14159  # Definición de la constante pi
    return pi * radius * radius  # Retorna el área calculada usando la fórmula pi * r^2

# Example 2
def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def find_max(numbers):
    """
    Encuentra el número máximo en una lista de números.

    Parámetros:
    numbers (list): Una lista de números.

    Retorna:
    int/float: El número máximo en la lista.
    """
    max_number = numbers[0]  # Inicializar con el primer elemento de la lista
    for number in numbers:  # Iterar sobre cada número en la lista
        if number > max_number:  # Comparar con el número máximo actual
            max_number = number  # Actualizar el número máximo si se encuentra uno mayor
    return max_number  # Retornar el número máximo encontrado

# Example 3
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sort(arr):
    """
    Ordena una lista de números utilizando el algoritmo de ordenamiento burbuja.

    Parámetros:
    arr (list): Una lista de números a ordenar.

    Retorna:
    list: La lista ordenada de menor a mayor.
    """
    n = len(arr)  # Obtener la cantidad de elementos en la lista
    for i in range(n):  # Recorrer cada elemento de la lista
        for j in range(0, n-i-1):  # Recorrer la lista hasta el elemento no ordenado
            if arr[j] > arr[j+1]:  # Comparar el elemento actual con el siguiente
                # Intercambiar los elementos si el actual es mayor que el siguiente
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr  # Devolver la lista ordenada

def bubble_sort(arr):
    """
    Ordena una lista de números utilizando el algoritmo de ordenamiento burbuja.

    :param arr: Una lista de números a ordenar.
    :type arr: list
    :return: La lista ordenada de menor a mayor.
    :rtype: list
    """
    n = len(arr)  # Obtener la cantidad de elementos en la lista
    for i in range(n):  # Recorrer cada elemento de la lista
        for j in range(0, n-i-1):  # Recorrer la lista hasta el elemento no ordenado
            if arr[j] > arr[j+1]:  # Comparar el elemento actual con el siguiente
                # Intercambiar los elementos si el actual es mayor que el siguiente
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr  # Devolver la lista ordenada