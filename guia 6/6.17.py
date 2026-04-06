import random
mapa = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]
max_val = -1
min_val = 101
suma = 0
for r in range(10):
    for c in range(10):
        v = mapa[r][c]
        suma += v
        if v > max_val: max_val = v
        if v < min_val: min_val = v
print(max_val, min_val, suma / 100)