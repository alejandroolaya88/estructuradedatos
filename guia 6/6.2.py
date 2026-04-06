def busqueda_binaria_nombres():
    nombres = input("Ingrese nombres separados por coma: ").split(",")
    nombres = [n.strip() for n in nombres]
    
    # Es obligatorio que esté ordenado para la búsqueda binaria
    nombres.sort()
    print(f"Lista ordenada: {nombres}")

    objetivo = input("Ingrese el nombre a buscar: ").strip()
    
    inicio = 0
    fin = len(nombres) - 1
    encontrado = -1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if nombres[medio] == objetivo:
            encontrado = medio
            break
        elif nombres[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    if encontrado != -1:
        print(f"Nombre '{objetivo}' encontrado en la posición {encontrado}.")
    else:
        print("El nombre no se encuentra en la lista.")

if __name__ == "__main__":
    busqueda_binaria_nombres()