class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircularSimple:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
            return
        t = self.cabeza
        while t.siguiente != self.cabeza: t = t.siguiente
        t.siguiente = nuevo
        nuevo.siguiente = self.cabeza

    def mostrar(self):
        if not self.cabeza: return
        elems = []
        t = self.cabeza
        while True:
            elems.append(str(t.dato))
            t = t.siguiente
            if t == self.cabeza: break
        print(" -> ".join(elems) + " -> (C)")

    def buscar(self, v):
        if not self.cabeza: return -1
        t = self.cabeza
        i = 0
        while True:
            if t.dato == v: return i
            t = t.siguiente
            i += 1
            if t == self.cabeza: break
        return -1

    def eliminar(self, v):
        if not self.cabeza: return
        act = self.cabeza
        prev = None
        while True:
            if act.dato == v:
                if prev:
                    prev.siguiente = act.siguiente
                    if act == self.cabeza: self.cabeza = prev.siguiente
                else:
                    t = self.cabeza
                    while t.siguiente != self.cabeza: t = t.siguiente
                    if self.cabeza == self.cabeza.siguiente: self.cabeza = None
                    else:
                        t.siguiente = self.cabeza.siguiente
                        self.cabeza = self.cabeza.siguiente
                return
            prev = act
            act = act.siguiente
            if act == self.cabeza: break

    def ordenar(self):
        if not self.cabeza: return
        c = True
        while c:
            c = False
            a = self.cabeza
            while a.siguiente != self.cabeza:
                if a.dato > a.siguiente.dato:
                    a.dato, a.siguiente.dato = a.siguiente.dato, a.dato
                    c = True
                a = a.siguiente

def menu():
    l = ListaCircularSimple()
    while True:
        print("\n--- CIRCULAR SIMPLE ---")
        op = input("1.Add 2.Show 3.Find 4.Del 5.Sort 6.Exit: ")
        if op=="1": l.agregar(int(input("Dato: ")))
        elif op=="2": l.mostrar()
        elif op=="3": print(l.buscar(int(input("Dato: "))))
        elif op=="4": l.eliminar(int(input("Dato: ")))
        elif op=="5": l.ordenar()
        elif op=="6": break

if __name__ == "__main__":
    menu()