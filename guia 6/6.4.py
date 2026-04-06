def recorrido_zigzag():
    # Ejemplo con una matriz predefinida de 3x3 para probar rápido
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Matriz actual:")
    for fila in matriz: print(fila)
    
    print("\nRecorrido en Zig-Zag:")
    resultado = []
    for i in range(len(matriz)):
        if i % 2 == 0:
            # Si la fila es par, de izquierda a derecha
            for j in range(len(matriz[i])):
                resultado.append(matriz[i][j])
        else:
            # Si la fila es impar, de derecha a izquierda
            for j in range(len(matriz[i]) - 1, -1, -1):
                resultado.append(matriz[i][j])
    
    print(resultado)

if __name__ == "__main__":
    recorrido_zigzag()