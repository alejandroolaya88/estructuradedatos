n = int(input("Introduce el valor de n para calcular el enésimo término: "))

if n <= 0:
    print("Por favor, introduce un número mayor a 0.")
elif n == 1:
    print(f"El término A1 es: 1")
elif n == 2:
    print(f"El término A2 es: 2")
else:
    a_prev2 = 1  # A1
    a_prev1 = 2  # A2
    a_n = 0
    
    for i in range(3, n + 1):
        a_n = a_prev1 + a_prev2
        a_prev2 = a_prev1
        a_prev1 = a_n
        
    print(f"El término A{n} de la serie es: {a_n}")
