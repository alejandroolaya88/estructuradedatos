class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = self.anterior = None

class ListaCircularDoble:
    def __init__(self):
        self.cabeza = None

    def agregar(self, d):
        n = Nodo(d)
        if not self.cabeza:
            self.cabeza = n
            n.siguiente = n.anterior = n
            return
        u = self.cabeza.anterior
        u.siguiente = n
        n.anterior = u
        n.siguiente = self.cabeza
        self.cabeza.anterior = n

    def mostrar(self):
        if not self.cabeza: return
        res = []
        t = self.cabeza
        while True:
            res.append(str(t.dato))
            t = t.siguiente
            if t == self.cabeza: break
        print(" <-> ".join(res) + " <-> (C)")

    def eliminar(self, v):
        if not self.cabeza: return
        a = self.cabeza
        while True:
            if a.dato == v:
                if a.siguiente == a: self.cabeza = None
                else:
                    a.anterior.siguiente = a.siguiente
                    a.siguiente.anterior = a.anterior
                    if a == self.cabeza: self.cabeza = a.siguiente
                return
            a = a.siguiente
            if a == self.cabeza: break

    def ordenar(self):
        if not self.cabeza: return
        s = True
        while s:
            s = False
            a = self.cabeza
            while a.siguiente != self.cabeza:
                if a.dato > a.siguiente.dato:
                    a.dato, a.siguiente.dato = a.siguiente.dato, a.dato
                    s = True
                a = a.siguiente

def menu():
    l = ListaCircularDoble()
    while True:
        print("\n--- CIRCULAR DOBLE ---")
        op = input("1.Add 2.Show 3.Del 4.Sort 5.Exit: ")
        if op=="1": l.agregar(int(input("Dato: ")))
        elif op=="2": l.mostrar()
        elif op=="3": l.eliminar(int(input("Valor: ")))
        elif op=="4": l.ordenar()
        elif op=="5": break

if __name__ == "__main__":
    menu()