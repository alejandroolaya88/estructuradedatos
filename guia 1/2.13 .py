def es_palindromo():
    print("Verificador de palindromos")
   
    palabra = input("Ingrese una palabra: ")
   
    # quitamos espacios y ponemos minusculas
    palabra_limpia = palabra.replace(" ", "").lower()
    
    palabra_invertida = palabra_limpia[::-1]
    
    print(f"\nPalabra original: {palabra}")
    print(f"Al revés: {palabra_invertida}")
    
    if palabra_limpia == palabra_invertida:
        return "Si es palindromo"
    else:
        return "no es palindromo"


print(es_palindromo())
