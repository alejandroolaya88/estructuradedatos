matriz = []
c = 1
for i in range(4):
    f = []
    for j in range(4):
        f.append(c)
        c += 1
    matriz.append(f)
for f in matriz:
    print(f)