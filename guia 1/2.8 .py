def calcular_velocidad_corredores():
    print("Cálculo de Velocidad Media (1.500m)")
    print("Ingrese el tiempo con un espacio (0 0 para finalizar)")
    
    DISTANCIA = 1500 
    
    while True:
        
        entrada = input("Tiempo del corredor (minutos segundos): ").split()
        
        # verificamos los dos valores
        if len(entrada) != 2:
            print("Por favor, ingrese dos números.")
            continue
            
        minutos = int(entrada[0])
        segundos = int(entrada[1])
        
        
        if minutos == 0 and segundos == 0:
            print("Fin de entrada de datos.")
            break
            
        # convertimos el tiempo a segundos
        tiempo_total_segundos = (minutos * 60) + segundos
        
        if tiempo_total_segundos > 0:
            #calculo
            velocidad = DISTANCIA / tiempo_total_segundos
            
            print(f"\nRESULTADOS:")
            print(f"Tiempo: {minutos} min {segundos} s")
            print(f"Velocidad Media: {velocidad:.2f} m/s")
            print("-" * 30)
        else:
            print("El tiempo debe ser mayor a cero.")


calcular_velocidad_corredores()
