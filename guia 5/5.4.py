suma = 0
contador = 0

while True:
    entrada = input("Introduce un número positivo (un número igual o menor que 0 para terminar): ").strip()
    
    if not entrada:
        continue
    
    numero = float(entrada)
    
    # Condición para terminar si es menor que cero o es igual a cero
    if numero <= 0:
        break
        
    suma += numero
    contador += 1

if contador > 0:
    media = suma / contador
    print(f"La media de los {contador} números introducidos es: {media}")
else:
    print("No se introdujeron números positivos antes del valor de terminación.")
