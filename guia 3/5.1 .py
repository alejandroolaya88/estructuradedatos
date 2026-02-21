suma = 0
contador = 0

while True:
    entrada = input("Introduce un número positivo (0 o uno negativo para terminar): ").strip()
    
    if not entrada:
        continue
    
    numero = float(entrada)
    
    if numero <= 0:
        break
        
    suma += numero
    contador += 1

if contador > 0:
    media = suma / contador
    print("La media de los números introducidos es:", media)
else:
    print("No se introdujeron números positivos.")
