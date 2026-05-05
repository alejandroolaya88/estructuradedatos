"""
=======================================================
  TALLER 9 — 10 ALGORITMOS DE BÚSQUEDA
  Estructura de Datos · UMB · 2026
=======================================================
  Algoritmos implementados:
    1. Búsqueda Lineal
    2. Búsqueda Binaria (iterativa)
    3. Búsqueda Binaria (recursiva)
    4. Búsqueda por Salto (Jump Search)
    5. Búsqueda Interpolada
    6. Búsqueda en Árbol Binario de Búsqueda (BST)
    7. Búsqueda DFS en Grafo
    8. Búsqueda BFS en Grafo
    9. Búsqueda en Tabla Hash
   10. Búsqueda en Trie (árbol de prefijos)
=======================================================
"""

import math
from collections import deque


# ─────────────────────────────────────────────────────
# 1. BÚSQUEDA LINEAL
#    Recorre cada elemento uno por uno.
#    Complejidad: O(n)  |  No requiere orden
# ─────────────────────────────────────────────────────
def busqueda_lineal(arr, objetivo):
    """
    Recorre el arreglo de izquierda a derecha buscando 'objetivo'.
    Retorna el índice si lo encuentra, -1 si no.
    """
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1


# ─────────────────────────────────────────────────────
# 2. BÚSQUEDA BINARIA — ITERATIVA
#    Divide el arreglo ordenado a la mitad en cada paso.
#    Complejidad: O(log n)  |  Requiere arreglo ordenado
# ─────────────────────────────────────────────────────
def busqueda_binaria(arr, objetivo):
    """
    Versión iterativa de búsqueda binaria.
    El arreglo DEBE estar ordenado de forma ascendente.
    Retorna el índice si encuentra el objetivo, -1 si no.
    """
    izquierda = 0
    derecha = len(arr) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izquierda = medio + 1   # Buscar en la mitad derecha
        else:
            derecha = medio - 1     # Buscar en la mitad izquierda

    return -1


# ─────────────────────────────────────────────────────
# 3. BÚSQUEDA BINARIA — RECURSIVA
#    Misma lógica que la iterativa pero con recursión.
#    Complejidad: O(log n)
# ─────────────────────────────────────────────────────
def busqueda_binaria_recursiva(arr, objetivo, izquierda=None, derecha=None):
    """
    Versión recursiva de búsqueda binaria.
    En la primera llamada, no es necesario pasar izquierda/derecha.
    """
    if izquierda is None:
        izquierda = 0
    if derecha is None:
        derecha = len(arr) - 1

    # Caso base: rango vacío, no se encontró
    if izquierda > derecha:
        return -1

    medio = (izquierda + derecha) // 2

    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, izquierda, medio - 1)


# ─────────────────────────────────────────────────────
# 4. BÚSQUEDA POR SALTO (JUMP SEARCH)
#    Salta bloques de tamaño √n, luego búsqueda lineal.
#    Complejidad: O(√n)  |  Requiere arreglo ordenado
# ─────────────────────────────────────────────────────
def busqueda_salto(arr, objetivo):
    """
    Divide el arreglo en bloques de tamaño √n.
    Salta bloques hasta encontrar uno que pueda contener el objetivo,
    luego hace búsqueda lineal dentro de ese bloque.
    """
    n = len(arr)
    paso = int(math.sqrt(n))   # Tamaño del bloque: raíz cuadrada de n
    inicio = 0
    fin = paso

    # Saltar bloques mientras el último elemento sea menor que el objetivo
    while fin < n and arr[fin] <= objetivo:
        inicio = fin
        fin += paso

    # Búsqueda lineal dentro del bloque encontrado
    for i in range(inicio, min(fin, n)):
        if arr[i] == objetivo:
            return i

    return -1


# ─────────────────────────────────────────────────────
# 5. BÚSQUEDA INTERPOLADA (INTERPOLATION SEARCH)
#    Estima la posición usando interpolación lineal.
#    Complejidad: O(log log n) datos uniformes | O(n) peor caso
# ─────────────────────────────────────────────────────
def busqueda_interpolada(arr, objetivo):
    """
    En lugar de ir siempre al centro (como binaria), estima dónde
    podría estar el objetivo usando la fórmula de interpolación:
        pos = bajo + ((objetivo - arr[bajo]) / (arr[alto] - arr[bajo])) * (alto - bajo)
    Muy eficiente cuando los datos están uniformemente distribuidos.
    """
    bajo = 0
    alto = len(arr) - 1

    while bajo <= alto and arr[bajo] <= objetivo <= arr[alto]:
        if bajo == alto:
            if arr[bajo] == objetivo:
                return bajo
            return -1

        # Fórmula de interpolación
        rango_valor = arr[alto] - arr[bajo]
        rango_indice = alto - bajo
        pos = bajo + int(((objetivo - arr[bajo]) / rango_valor) * rango_indice)

        if arr[pos] == objetivo:
            return pos
        elif arr[pos] < objetivo:
            bajo = pos + 1
        else:
            alto = pos - 1

    return -1


# ─────────────────────────────────────────────────────
# 6. BÚSQUEDA EN ÁRBOL BINARIO DE BÚSQUEDA (BST)
#    Navega el árbol comparando con cada nodo.
#    Complejidad: O(log n) promedio | O(n) peor caso (árbol degenerado)
# ─────────────────────────────────────────────────────
class NodoBST:
    """Nodo para el Árbol Binario de Búsqueda."""
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBST:
    """Árbol Binario de Búsqueda con inserción y búsqueda."""

    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        """Inserta un valor en el BST."""
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if nodo is None:
            return NodoBST(valor)
        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, valor)
        return nodo

    def buscar(self, objetivo):
        """
        Busca un valor en el BST.
        Retorna True si existe, False si no.
        """
        return self._buscar_recursivo(self.raiz, objetivo)

    def _buscar_recursivo(self, nodo, objetivo):
        # Caso base: nodo vacío o valor encontrado
        if nodo is None:
            return False
        if nodo.valor == objetivo:
            return True
        # Navegar izquierda o derecha según comparación
        if objetivo < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, objetivo)
        else:
            return self._buscar_recursivo(nodo.derecho, objetivo)


# ─────────────────────────────────────────────────────
# 7. BÚSQUEDA DFS EN GRAFO (Depth-First Search)
#    Explora en profundidad usando una pila (stack).
#    Complejidad: O(V + E)  |  V=vértices, E=aristas
# ─────────────────────────────────────────────────────
def busqueda_dfs(grafo, inicio, objetivo):
    """
    Búsqueda en profundidad en un grafo representado como diccionario
    de listas de adyacencia. Explora cada rama completamente antes
    de pasar a la siguiente.
    Retorna True si encuentra el objetivo, False si no.
    """
    visitados = set()
    pila = [inicio]

    while pila:
        nodo = pila.pop()   # LIFO: último en entrar, primero en salir

        if nodo == objetivo:
            return True

        if nodo not in visitados:
            visitados.add(nodo)
            # Agregar vecinos no visitados a la pila
            for vecino in grafo.get(nodo, []):
                if vecino not in visitados:
                    pila.append(vecino)

    return False


# ─────────────────────────────────────────────────────
# 8. BÚSQUEDA BFS EN GRAFO (Breadth-First Search)
#    Explora nivel por nivel usando una cola (queue).
#    Complejidad: O(V + E)
# ─────────────────────────────────────────────────────
def busqueda_bfs(grafo, inicio, objetivo):
    """
    Búsqueda en anchura. Explora todos los nodos a distancia 1
    antes de pasar a distancia 2, etc. Garantiza el camino más
    corto en grafos no ponderados.
    Retorna la lista del camino si lo encuentra, [] si no.
    """
    visitados = set([inicio])
    cola = deque([[inicio]])    # Cola de caminos (no solo nodos)

    while cola:
        camino = cola.popleft()  # FIFO: primero en entrar, primero en salir
        nodo = camino[-1]

        if nodo == objetivo:
            return camino   # Retorna el camino completo

        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = camino + [vecino]
                cola.append(nuevo_camino)

    return []


# ─────────────────────────────────────────────────────
# 9. BÚSQUEDA EN TABLA HASH
#    Acceso directo mediante función hash.
#    Complejidad: O(1) promedio
# ─────────────────────────────────────────────────────
class TablaHash:
    """
    Tabla Hash con encadenamiento para resolver colisiones.
    Usa el operador % para mapear claves a índices.
    """

    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.tabla = [[] for _ in range(capacidad)]  # Lista de listas (encadenamiento)

    def _hash(self, clave):
        """Función hash simple: módulo de la suma de valores ASCII."""
        return sum(ord(c) for c in str(clave)) % self.capacidad

    def insertar(self, clave, valor):
        """Inserta un par clave-valor en la tabla."""
        indice = self._hash(clave)
        # Si la clave ya existe, actualizar su valor
        for par in self.tabla[indice]:
            if par[0] == clave:
                par[1] = valor
                return
        self.tabla[indice].append([clave, valor])

    def buscar(self, clave):
        """
        Busca una clave en la tabla hash.
        Retorna el valor asociado, o None si no existe.
        """
        indice = self._hash(clave)
        for par in self.tabla[indice]:
            if par[0] == clave:
                return par[1]   # Retorna el valor asociado
        return None


# ─────────────────────────────────────────────────────
# 10. BÚSQUEDA EN TRIE (ÁRBOL DE PREFIJOS)
#     Busca palabras o prefijos carácter por carácter.
#     Complejidad: O(m)  |  m = longitud de la palabra
# ─────────────────────────────────────────────────────
class NodoTrie:
    """Nodo del Trie con mapa de hijos y flag de fin de palabra."""
    def __init__(self):
        self.hijos = {}          # Diccionario: carácter → NodoTrie
        self.es_fin_palabra = False


class Trie:
    """
    Árbol de prefijos. Cada camino desde la raíz hasta un nodo
    marcado como fin representa una palabra completa.
    Ideal para autocompletado y búsqueda de prefijos.
    """

    def __init__(self):
        self.raiz = NodoTrie()

    def insertar(self, palabra):
        """Inserta una palabra en el Trie carácter por carácter."""
        nodo = self.raiz
        for caracter in palabra:
            if caracter not in nodo.hijos:
                nodo.hijos[caracter] = NodoTrie()
            nodo = nodo.hijos[caracter]
        nodo.es_fin_palabra = True   # Marcar el final de la palabra

    def buscar(self, palabra):
        """
        Busca una palabra EXACTA en el Trie.
        Retorna True si existe como palabra completa, False si no.
        """
        nodo = self.raiz
        for caracter in palabra:
            if caracter not in nodo.hijos:
                return False
            nodo = nodo.hijos[caracter]
        return nodo.es_fin_palabra

    def buscar_prefijo(self, prefijo):
        """
        Verifica si existe alguna palabra que comience con 'prefijo'.
        Útil para autocompletado.
        """
        nodo = self.raiz
        for caracter in prefijo:
            if caracter not in nodo.hijos:
                return False
            nodo = nodo.hijos[caracter]
        return True


# =======================================================
# DEMOSTRACIÓN DE TODOS LOS ALGORITMOS
# =======================================================
if __name__ == "__main__":
    print("=" * 55)
    print("  TALLER 9 — ALGORITMOS DE BÚSQUEDA")
    print("=" * 55)

    # ── Datos de prueba ──────────────────────────────
    lista_desordenada = [64, 34, 25, 12, 22, 11, 90, 7, 55]
    lista_ordenada    = [2, 5, 8, 12, 16, 23, 38, 42, 56, 72, 91]

    # ── 1. Búsqueda Lineal ───────────────────────────
    idx = busqueda_lineal(lista_desordenada, 22)
    print(f"\n1. Búsqueda Lineal → '22' en índice: {idx}")

    # ── 2. Búsqueda Binaria Iterativa ────────────────
    idx = busqueda_binaria(lista_ordenada, 42)
    print(f"2. Búsqueda Binaria (iterativa) → '42' en índice: {idx}")

    # ── 3. Búsqueda Binaria Recursiva ────────────────
    idx = busqueda_binaria_recursiva(lista_ordenada, 16)
    print(f"3. Búsqueda Binaria (recursiva) → '16' en índice: {idx}")

    # ── 4. Búsqueda por Salto ────────────────────────
    idx = busqueda_salto(lista_ordenada, 56)
    print(f"4. Búsqueda por Salto → '56' en índice: {idx}")

    # ── 5. Búsqueda Interpolada ──────────────────────
    idx = busqueda_interpolada(lista_ordenada, 23)
    print(f"5. Búsqueda Interpolada → '23' en índice: {idx}")

    # ── 6. Búsqueda BST ──────────────────────────────
    arbol = ArbolBST()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(val)
    encontrado = arbol.buscar(40)
    print(f"6. Búsqueda BST → ¿Existe 40?: {encontrado}")
    no_encontrado = arbol.buscar(99)
    print(f"   Búsqueda BST → ¿Existe 99?: {no_encontrado}")

    # ── 7. DFS en Grafo ──────────────────────────────
    grafo = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [], 'E': [], 'F': []
    }
    resultado_dfs = busqueda_dfs(grafo, 'A', 'F')
    print(f"7. DFS → ¿Existe camino A→F?: {resultado_dfs}")

    # ── 8. BFS en Grafo ──────────────────────────────
    camino = busqueda_bfs(grafo, 'A', 'E')
    print(f"8. BFS → Camino más corto A→E: {' → '.join(camino)}")

    # ── 9. Tabla Hash ────────────────────────────────
    tabla = TablaHash()
    tabla.insertar("nombre", "Carlos")
    tabla.insertar("edad", 21)
    tabla.insertar("ciudad", "Bogotá")
    nombre = tabla.buscar("nombre")
    ciudad = tabla.buscar("ciudad")
    nada   = tabla.buscar("pais")
    print(f"9. Hash Table → nombre: '{nombre}', ciudad: '{ciudad}', pais: '{nada}'")

    # ── 10. Trie ─────────────────────────────────────
    trie = Trie()
    for palabra in ["algoritmo", "array", "arbol", "busqueda", "binaria", "grafo"]:
        trie.insertar(palabra)

    print(f"10. Trie → ¿Existe 'algoritmo'?:  {trie.buscar('algoritmo')}")
    print(f"    Trie → ¿Existe 'algo'?:        {trie.buscar('algo')}")
    print(f"    Trie → ¿Prefijo 'algo' existe?: {trie.buscar_prefijo('algo')}")
    print(f"    Trie → ¿Prefijo 'bus' existe?:  {trie.buscar_prefijo('bus')}")

    print("\n" + "=" * 55)
    print("  Todos los algoritmos ejecutados con éxito ✓")
    print("=" * 55)
