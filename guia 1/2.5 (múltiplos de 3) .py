def multiplos_de_tres():
    print("Visualización de los múltiplos de 3")
    
    for numero in range(3, 100, 3): # primer 3 es punto de partida el 100 es el limite y el ultimo 3 es el incremento de cada paso
        print(f"Número actual: {numero}")
        
print(multiplos_de_tres())
