import random #Vamos a generar numeros aleatorios para no tener que digitar 100 numeros

nums_pos = []
nums_neg = []

opcion = input("¿Deseas generar los 100 números aleatoriamente? (si/no): ").strip().lower() #aun asi dejamos la opcion para ingresarlos manualmente

for i in range(1, 101):
    if opcion == "si":
        # Genera números con decimales entre -100 y 100
        numero = random.uniform(-100, 100)
    else:
        while True:
            try:
                entrada = input(f"Introduce el número {i} de 100: ")
                numero = float(entrada)
                break
            except ValueError:
                print("Error: Ingresa un número válido.")
    
    if numero > 0:
        nums_pos.append(numero)
    elif numero < 0:
        nums_neg.append(numero)

# Mostrar los números generados para verificar aleatoriedad
if opcion == "si":
    print("\n Números Generados ")
    todos = nums_pos + nums_neg
    for i in range(0, len(todos), 5):  
        print([round(n, 2) for n in todos[i:i+5]])

print("\nRESULTADOS ")
if nums_pos:
    media_pos = sum(nums_pos) / len(nums_pos)
    print(f"Positivos: {len(nums_pos)} números. Media: {round(media_pos, 2)}")
else:
    print("No hubo números positivos.")

if nums_neg:
    media_neg = sum(nums_neg) / len(nums_neg)
    print(f"Negativos: {len(nums_neg)} números. Media: {round(media_neg, 2)}")
else:
    print("No hubo números negativos.")
