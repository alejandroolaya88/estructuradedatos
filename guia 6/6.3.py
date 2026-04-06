def operaciones_matrices():
    filas = int(input("Ingrese número de filas: "))
    columnas = int(input("Ingrese número de columnas: "))
    
    matriz = []
    print("Ingrese los valores de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Elemento [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)

    # Suma de elementos
    suma_total = sum(sum(fila) for fila in matriz)

    # Matriz Transpuesta
    transpuesta = [[matriz[j][i] for j in range(filas)] for i in range(columnas)]

    print("\n--- Matriz Original ---")
    for f in matriz:
        print(f)
        
    print(f"\nSuma total de elementos: {suma_total}")

    print("\n--- Matriz Transpuesta ---")
    for f in transpuesta:
        print(f)

if __name__ == "__main__":
    operaciones_matrices()