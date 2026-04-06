def gestionar_calificaciones():
    n = int(input("Ingrese la cantidad de calificaciones: "))
    notas = []

    for i in range(n):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)

    # Cálculos básicos
    promedio = sum(notas) / n
    nota_max = max(notas)
    nota_min = min(notas)

    # Ordenamiento Burbuja
    for i in range(n):
        for j in range(0, n - i - 1):
            if notas[j] > notas[j + 1]:
                notas[j], notas[j + 1] = notas[j + 1], notas[j]

    print("\n--- Resultados ---")
    print(f"Promedio: {promedio:.2f}")
    print(f"Nota más alta: {nota_max}")
    print(f"Nota más baja: {nota_min}")
    print(f"Notas ordenadas: {notas}")

if __name__ == "__main__":
    gestionar_calificaciones()