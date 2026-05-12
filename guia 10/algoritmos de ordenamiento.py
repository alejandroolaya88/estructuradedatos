def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        hubo_intercambio = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                hubo_intercambio = True
        if not hubo_intercambio:
            break
    return arr


def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        idx_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[idx_min]:
                idx_min = j
        arr[i], arr[idx_min] = arr[idx_min], arr[i]
    return arr


def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr


def shell_sort(arr):
    arr = arr.copy()
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()
    medio = len(arr) // 2
    izquierda = merge_sort(arr[:medio])
    derecha   = merge_sort(arr[medio:])
    return _merge(izquierda, derecha)

def _merge(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


def quick_sort(arr):
    arr = arr.copy()
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

def _quick_sort_helper(arr, bajo, alto):
    if bajo < alto:
        idx_pivote = _particionar(arr, bajo, alto)
        _quick_sort_helper(arr, bajo, idx_pivote - 1)
        _quick_sort_helper(arr, idx_pivote + 1, alto)

def _particionar(arr, bajo, alto):
    pivote = arr[alto]
    i = bajo - 1
    for j in range(bajo, alto):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1


def heap_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)
    return arr

def _heapify(arr, n, i):
    mayor = i
    izq   = 2 * i + 1
    der   = 2 * i + 2
    if izq < n and arr[izq] > arr[mayor]:
        mayor = izq
    if der < n and arr[der] > arr[mayor]:
        mayor = der
    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        _heapify(arr, n, mayor)


def counting_sort(arr):
    if not arr:
        return []
    maximo = max(arr)
    conteo = [0] * (maximo + 1)
    for num in arr:
        conteo[num] += 1
    resultado = []
    for valor, cantidad in enumerate(conteo):
        resultado.extend([valor] * cantidad)
    return resultado


def radix_sort(arr):
    if not arr:
        return []
    arr = arr.copy()
    maximo = max(arr)
    exp = 1
    while maximo // exp > 0:
        arr = _counting_sort_por_digito(arr, exp)
        exp *= 10
    return arr

def _counting_sort_por_digito(arr, exp):
    n = len(arr)
    salida = [0] * n
    conteo = [0] * 10
    for num in arr:
        conteo[(num // exp) % 10] += 1
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]
    for i in range(n - 1, -1, -1):
        digito = (arr[i] // exp) % 10
        salida[conteo[digito] - 1] = arr[i]
        conteo[digito] -= 1
    return salida


def bucket_sort(arr):
    if not arr:
        return []
    arr = arr.copy()
    n = len(arr)
    maximo = max(arr)
    minimo = min(arr)
    rango  = maximo - minimo
    if rango == 0:
        return arr
    cubetas = [[] for _ in range(n)]
    for num in arr:
        idx = int((num - minimo) / rango * (n - 1))
        cubetas[idx].append(num)
    resultado = []
    for cubeta in cubetas:
        cubeta.sort()
        resultado.extend(cubeta)
    return resultado


if __name__ == "__main__":
    datos = [64, 34, 25, 12, 22, 11, 90, 7, 55, 42]
    print(f"Original:       {datos}")
    print(f"Bubble Sort:    {bubble_sort(datos)}")
    print(f"Selection Sort: {selection_sort(datos)}")
    print(f"Insertion Sort: {insertion_sort(datos)}")
    print(f"Shell Sort:     {shell_sort(datos)}")
    print(f"Merge Sort:     {merge_sort(datos)}")
    print(f"Quick Sort:     {quick_sort(datos)}")
    print(f"Heap Sort:      {heap_sort(datos)}")
    print(f"Counting Sort:  {counting_sort(datos)}")
    print(f"Radix Sort:     {radix_sort(datos)}")
    print(f"Bucket Sort:    {bucket_sort(datos)}")