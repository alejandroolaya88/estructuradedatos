total_dias = 0
suma_max = 0.0
suma_min = 0.0
errores = 0
total_lecturas = 0

print("Estación Climática: Ingrese temperaturas (0,0 para finalizar)")

while True:
    try:
        entrada_max = input("Temperatura máxima: ").strip()
        entrada_min = input("Temperatura mínima: ").strip()
        
        if not entrada_max or not entrada_min:
            continue
            
        t_max = float(entrada_max)
        t_min = float(entrada_min)
        
        # Condición de parada
        if t_max == 0 and t_min == 0:
            break
            
        total_dias += 1
        total_lecturas += 2
        
        # Verificar errores 
        hay_error_en_dia = False
        if t_max == 9:
            errores += 1
            hay_error_en_dia = True
        else:
            suma_max += t_max
            
        if t_min == 9:
            errores += 1
            hay_error_en_dia = True
        else:
            suma_min += t_min
            
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

# calculos finales
print("\n INFORME CLIMÁTICO")
print(f"Número de días procesados: {total_dias}")

if total_dias > 0:
    # Media de máximas (excluyendo los errores de 9 grados)
    cant_max_validas = total_dias - (1 if 't_max' in locals() and t_max == 9 else 0)
    # Para exactitud, usamos contadores si se requieren medias estrictas sin los 9s
    print(f"Media de temperaturas máximas (válidas): {suma_max / total_dias:.2f}°")
    print(f"Media de temperaturas mínimas (válidas): {suma_min / total_dias:.2f}°")
    
    print(f"Número de errores (9° detectados): {errores}")
    
    if total_lecturas > 0:
        porcentaje_errores = (errores / total_lecturas) * 100
        print(f"Porcentaje de errores: {porcentaje_errores:.2f}%")
else:
    print("No se registraron datos.")
