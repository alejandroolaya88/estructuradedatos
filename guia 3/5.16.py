N = 15 #tamaño de la tabla

# encabezado

print("      ", end="") # alineamiento

for i in range(1, N + 1):
    print(f"{i:4}", end="")
print("\n** " + "** " * N) 

# tabla
for i in range(1, N + 1):
    print(f"{i:<2}* ", end=" ")
    
    # resultados
    for j in range(1, N + 1):
        producto = i * j
        print(f"{producto:4}", end="")
    
    print()
