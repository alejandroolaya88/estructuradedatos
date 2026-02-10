'''  #EJERCICIO (A) SUMAR DOS NUMEROS
def sumar_enteros(a, b):
    print(f"Sumando {a} + {b}")
    resultado = a + b
    return f"El resultado de la suma es: {resultado}"

# quitar los apostrofes para probar si funciona también se pueden cambiar los valores de 15 y 10
print(sumar_enteros(15, 10))
 ''' # FIN EJERCICIO (A)


''' #EJERCICIO (B) RESTAR DOS NUMEROS
def restar_enteros(a, b):
    print(f"Restando {a} - {b}")
    resultado = a - b
    return f"El resultado de la resta es: {resultado}"

# quitar los apostrofes para probar si funciona también se pueden cambiar los valores de 50 y 20
print(restar_enteros(50, 20))
''' # FIN EJERCICIO (B)


''' #EJERCICIO (C) MULTIPLICAR DOS NUMEROS
def multiplicar_enteros(a, b):
    print(f"Multiplicando {a} * {b}")
    resultado = a * b
    return f"El resultado de la multiplicación es: {resultado}"

# quitar los apostrofes para probar si funciona también se pueden cambiar los valores de 8 y 7
print(multiplicar_enteros(8, 7))
''' # FIN EJERCICIO (C)


''' #EJERCICIO (D) DIVIDIR DOS NUMEROS
def dividir_enteros(a, b):
    print(f"Dividiendo {a} / {b}")
    
    # validamos que no se divida por cero por que es imposible
    if b == 0:
        return "Error: No se puede dividir por cero."
    
    # usar// para división entera o / para división con decimales
    resultado = a / b
    return f"El resultado de la división es: {resultado}"

# quitar los apostrofes para probar si funciona también se pueden cambiar los valores de 100, 4
print(dividir_enteros(100, 4))
''' # FIN EJERCICIO (D)
