def calculo_triangulo():
    print("Calculadora de Área de Triángulos")
    
    
    try:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        
        
        if base <= 0 or altura <= 0:
            return "Error: La base y la altura deben ser mayores que cero."
        
        # calculo base x altura
        superficie = (base * altura) / 2
        
        print(f"\nDatos del triángulo:")
        print(f"Base: {base} | Altura: {altura}")
        return f"La superficie (área) es: {superficie}"
        
    except ValueError:
        return "Error: Por favor, ingrese solo valores numéricos."


print(calculo_triangulo())
