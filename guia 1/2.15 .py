def calcular_interes_bancario():
    print("Simulador de deposito bancario")
    
    try:

        capital_inicial = float(input("Ingrese el capital a depositar (pesos): "))
        tasa_interes_anual = float(input("Ingrese la tasa de interés anual (ej: 6 para 6%): "))
        semanas = int(input("ingrese la duracion del deposito en semanas: "))
        
        tasa_decimal = tasa_interes_anual / 100
        
        dias_totales = semanas * 7
        
        interes_diario = (tasa_decimal * capital_inicial) / 365
               
        interes_total_acumulado = interes_diario * dias_totales
        capital_final = capital_inicial + interes_total_acumulado
        
        print(f"\nRESULTADOS DEL DEPÓSITO" )
        print(f"Días transcurridos: {dias_totales} días")
        print(f"Interés generado por día: {interes_diario:.4f} pesos")
        print(f"Total intereses ganados: {interes_total_acumulado:.2f} pesos")
        return f"Capital total acumulado: {capital_final:.2f} pesos"
        
    except ValueError:
        return "Error: Ingrese valores numéricos válidos."


print(calcular_interes_bancario())
