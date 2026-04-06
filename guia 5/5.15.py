import random #ponemos random para generar salarios aleatorios y no tener que digitar 50 datos

salarios_altos = 0   # mas de 300.000
salarios_medios = 0  # entre 100.000 y 300.000
salarios_bajos = 0   # menos de 100.000

print("Estadísticas de Salarios de la Empresa (50 empleados)")
opcion = input("¿Deseas generar los 50 salarios aleatoriamente? (si/no): ").strip().lower() 
#aun asi dejamos la opcion por si se quiere ingresar manualmente los datos ya que el aleatorio es para las pruebas de si esta funcionando el codigo
for i in range(1, 51):
    if opcion == "si":
        # generamos salarios aleatorios entre 50.000 y 500.000 para probar los rangos
        salario = random.randint(50000, 500000)
    else:
        while True:
            try:
                entrada = input(f"Introduce el salario del empleado {i}: ")
                salario = float(entrada)
                break
            except ValueError:
                print("Error: Por favor introduce un número válido.")

    # clasificacion de salarios
    if salario > 300000:
        salarios_altos += 1
    elif 100000 <= salario <= 300000:
        salarios_medios += 1
    else:
        salarios_bajos += 1

print("\n RESULTADOS DE LA EMPRESA ")
print(f"a) Empleados con salarios altos (> 300.000): {salarios_altos}")
print(f"b) Empleados con salarios medios (entre 100.000 - 300.000): {salarios_medios}")
print(f"c) Empleados con salarios bajos (< 100.000): {salarios_bajos}")
