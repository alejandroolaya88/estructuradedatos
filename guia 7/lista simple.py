class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        ultimo = self.cabeza
        while ultimo.siguiente:
            ultimo = ultimo.siguiente
        ultimo.siguiente = nuevo_nodo

    def mostrar(self):
        if not self.cabeza:
            print("La lista está vacía.")
            return
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(" -> ".join(elementos))

    def buscar(self, valor):
        actual = self.cabeza
        indice = 0
        while actual:
            if actual.dato == valor:
                return indice
            actual = actual.siguiente
            indice += 1
        return -1

    def actualizar(self, indice, nuevo_dato):
        actual = self.cabeza
        indice_actual = 0
        while actual:
            if indice_actual == indice:
                actual.dato = nuevo_dato
                return True
            actual = actual.siguiente
            indice_actual += 1
        return False

    def eliminar(self, valor):
        actual = self.cabeza
        if actual and actual.dato == valor:
            self.cabeza = actual.siguiente
            return
        previo = None
        while actual and actual.dato != valor:
            previo = actual
            actual = actual.siguiente
        if actual:
            previo.siguiente = actual.siguiente

    def ordenar(self):
        if not self.cabeza or not self.cabeza.siguiente:
            return
        fin = None
        while fin != self.cabeza.siguiente:
            p = self.cabeza
            while p.siguiente != fin:
                q = p.siguiente
                if p.dato > q.dato:
                    p.dato, q.dato = q.dato, p.dato
                p = p.siguiente
            fin = p

def menu():
    lista = ListaEnlazadaSimple()
    while True:
        print("\n--- MENU LISTA SIMPLE ---")
        print("1. Agregar dato")
        print("2. Mostrar lista")
        print("3. Buscar dato")
        print("4. Actualizar por índice")
        print("5. Eliminar por valor")
        print("6. Ordenar lista")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            d = int(input("Ingrese el número: "))
            lista.agregar(d)
        elif opcion == "2":
            lista.mostrar()
        elif opcion == "3":
            v = int(input("Valor a buscar: "))
            res = lista.buscar(v)
            print(f"Encontrado en índice: {res}" if res != -1 else "No encontrado")
        elif opcion == "4":
            idx = int(input("Índice: "))
            nd = int(input("Nuevo valor: "))
            lista.actualizar(idx, nd)
        elif opcion == "5":
            v = int(input("Valor a eliminar: "))
            lista.eliminar(v)
        elif opcion == "6":
            lista.ordenar()
            print("Lista ordenada.")
        elif opcion == "7":
            break

if __name__ == "__main__":
    menu()
