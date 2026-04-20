class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaEnlazadaDoble:
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
        nuevo_nodo.anterior = ultimo

    def mostrar(self):
        if not self.cabeza:
            print("Lista vacía")
            return
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(" <-> ".join(elementos))

    def buscar(self, valor):
        actual = self.cabeza
        idx = 0
        while actual:
            if actual.dato == valor: return idx
            actual = actual.siguiente
            idx += 1
        return -1

    def actualizar(self, indice, dato):
        actual = self.cabeza
        i = 0
        while actual:
            if i == indice:
                actual.dato = dato
                return
            actual = actual.siguiente
            i += 1

    def eliminar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.dato == valor:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                return
            actual = actual.siguiente

    def ordenar(self):
        if not self.cabeza: return
        cambio = True
        while cambio:
            cambio = False
            curr = self.cabeza
            while curr.siguiente:
                if curr.dato > curr.siguiente.dato:
                    curr.dato, curr.siguiente.dato = curr.siguiente.dato, curr.dato
                    cambio = True
                curr = curr.siguiente

def menu():
    lista = ListaEnlazadaDoble()
    while True:
        print("\n--- MENU LISTA DOBLE ---")
        print("1. Agregar", "2. Mostrar", "3. Buscar", "4. Actualizar", "5. Eliminar", "6. Ordenar", "7. Salir")
        op = input("Opción: ")
        if op == "1": lista.agregar(int(input("Dato: ")))
        elif op == "2": lista.mostrar()
        elif op == "3": print(f"Índice: {lista.buscar(int(input('Buscar: ')))}")
        elif op == "4": lista.actualizar(int(input("Idx: ")), int(input("Dato: ")))
        elif op == "5": lista.eliminar(int(input("Eliminar: ")))
        elif op == "6": lista.ordenar()
        elif op == "7": break

if __name__ == "__main__":
    menu()