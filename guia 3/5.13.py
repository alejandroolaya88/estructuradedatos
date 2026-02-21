mayores_65 = 0

print("Lectura de empleados de la empresa (escribe 'fin' para terminar)")

while True:
    entrada = input("Introduce la edad del empleado (o 'fin'): ").strip().lower()
    
    if entrada == 'fin':
        break
    
    try:
        edad = int(entrada)
        if edad > 65:
            mayores_65 += 1
    except ValueError:
        print("Error: Ingresa una edad válida o 'fin'.")

print(f"existen trabajadores mayores de 65 años en un número de ... {mayores_65}")
