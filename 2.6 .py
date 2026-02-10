def num_mayor():
    print("2Buscador del Número Mayor")
    
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    n3 = float(input("Ingrese el tercer número: "))
    n4 = float(input("Ingrese el cuarto número: "))

    mayor = n1
    
    if n2 > mayor:
        mayor = n2
    
    if n3 > mayor:
        mayor = n3
        
    if n4 > mayor:
        mayor = n4
    
    print(f"Los números ingresados fueron: {n1}, {n2}, {n3}, {n4}")
    return f"El mayor de todos es: {mayor}"

print(num_mayor())
