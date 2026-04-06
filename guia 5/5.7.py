notables = []

while True:
    entrada = input("Introduce la nota (o escribe 'fin' para terminar): ").strip().lower()
    
    if entrada == 'fin':
        break
        
    try:
        nota = float(entrada)
        
        if 7 <= nota < 9:
            notables.append(nota)
            
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número o 'fin'.")

if len(notables) > 0:
    print(f"Se encontraron {len(notables)} notas notables:")
    for n in notables:
        print(n)
else:
    print("No se registraron notas en el rango de notables (7 a 8.9).")
