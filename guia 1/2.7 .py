def verificar_suma_de_dos():
    print("Uno es la suma de los otros dos?")
    
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
 
    if a + b == c:
        return f"Si {a} + {b} = {c}"
    elif a + c == b:
        return f"Si {a} + {c} = {b}"
    elif b + c == a:
        return f"Si {b} + {c} = {a}"
    else:
        return "No hay ningún número que sea la suma de los otros dos."
    
print(verificar_suma_de_dos())
