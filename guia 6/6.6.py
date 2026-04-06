v = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = len([x for x in v if x % 2 == 0])
impares = len(v) - pares
print(pares, impares)
