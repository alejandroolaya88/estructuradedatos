aprobados = 0
total_estudiantes = 0

while True:
    entrada = input("Introduce la calificación (o escribe 'fin' para terminar): ").strip().lower()
    
    if entrada == 'fin':
        break
        
    try:
        nota = float(entrada)
        total_estudiantes += 1
        
        if nota >= 3:
            aprobados += 1
    except ValueError:
        print("Por favor, introduce un número válido o 'fin'.")

print(f"Total de estudiantes evaluados: {total_estudiantes}")
print(f"Número total de aprobados: {aprobados}")
