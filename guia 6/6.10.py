estudiantes = []
notas = []
for i in range(20):
    estudiantes.append(input())
    notas.append(float(input()))

print(sum(notas)/20)
idx_max = notas.index(max(notas))
print(estudiantes[idx_max])
