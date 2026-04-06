# a) Estructura repetir se necesita el break para cerrar el bucle
suma_a = 0
i = 1
while True:
    suma_a += i
    i += 1
    if i > 100:
        break
print("Suma con estructura repetir (1 a 100):", suma_a)

# b) Estructura mientras (while)
suma_b = 0
i = 1
while i <= 100:
    suma_b += i
    i += 1
print("Suma con estructura mientras (1 a 100):", suma_b)

# c) Estructura desde (for)
suma_c = 0
for i in range(1, 101):
    suma_c += i
print("Suma con estructura desde (1 a 100):", suma_c)

#Para todos se usa contadores para que sea más sencillo
