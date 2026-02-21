total_articulos_a = 0
total_articulos_b = 0
importe_total_a = 0.0
importe_total_b = 0.0

while True:
    codigo = input("Introduce el código del artículo (A, B o X para terminar): ").strip().upper()
    
    if codigo == 'X':
        break
        
    if codigo not in ['A', 'B']:
        print("Código no válido. Use A, B o X.")
        continue
    
    try:
        precio = float(input(f"Introduce el precio unitario del artículo {codigo}: "))
        cantidad = int(input(f"Introduce el número de artículos de tipo {codigo}: "))
        
        if codigo == 'A':
            total_articulos_a += cantidad
            importe_total_a += (precio * cantidad)
        elif codigo == 'B':
            total_articulos_b += cantidad
            importe_total_b += (precio * cantidad)
            
    except ValueError:
        print("Error: El precio y la cantidad deben ser valores numéricos.")

print("\n RESULTADOS POR CATEGORÍA ")
print(f"Categoría A:")
print(f"  - Total de artículos: {total_articulos_a}")
print(f"  - Importe total: ${importe_total_a:.2f}")

print(f"Categoría B:")
print(f"  - Total de artículos: {total_articulos_b}")
print(f"  - Importe total: ${importe_total_b:.2f}")
