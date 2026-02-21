import math

while True:
    try:
        n = int(input("Introduce un entero positivo n (> 1): "))
        if n > 1:
            break
        else:
            print("El número debe ser mayor que 1.")
    except ValueError:
        print("Error: Por favor, introduce un número entero.")

# comprobacion primo
es_primo = True

limite = int(math.sqrt(n))

for i in range(2, limite + 1):
    if n % i == 0:
        es_primo = False
        divisor_encontrado = i 
        break

if es_primo:
    print(f"El número {n} es PRIMO.")
else:
    print(f"El número {n} es COMPUESTO (es divisible por {divisor_encontrado}).")
