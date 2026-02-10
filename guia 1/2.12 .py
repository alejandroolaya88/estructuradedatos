def calc_salariosemanal():
    print("Calculadora de Nómina Semanal")
    
    try:
        tarifa = float(input("Ingrese la tarifa por hora: "))
        dias_laborales = int(input("Cuantos dias trabajo esta semana?: "))
        
        total_horas_semana = 0
        
        for i in range(1, dias_laborales + 1):
            horas_dia = float(input(f"Horas trabajadas el dia {i}: "))
            total_horas_semana += horas_dia
        
        salario_total = total_horas_semana * tarifa
        
        print("\nRESUMEN")
        print(f"Total de horas trabajadas: {total_horas_semana}h")
        print(f"Tarifa horaria aplicada: ${tarifa}")
        return f"El salario semanal total es: ${salario_total:.2f}"
        
    except ValueError:
        return "Error: Ingrese valores numéricos válidos."

print(calc_salariosemanal())
