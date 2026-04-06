import math

x = float(input("Introduce el valor de x: "))

n_entero = int(input("Introduce el valor de N (número de términos): "))
suma_a = 0

for i in range(n_entero + 1):
    termino = (x**i) / math.factorial(i)
    suma_a += termino

print(f"Resultado (a) con N={n_entero}: {suma_a}")

E = 1e-4
suma_b = 0
i = 0
while True:
    termino = (x**i) / math.factorial(i)
    suma_b += termino
    if termino < E:
        break
    i += 1

print(f"Resultado (b) con E={E}: {suma_b} (alcanzado en N={i})")
