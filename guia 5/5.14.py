C = float(input("Introduce el capital inicial (C): "))
R = float(input("Introduce el tipo de interés anual en porcentaje (R%): "))

# Convertir porcentaje a decimal
interes_decimal = R / 100
capital_objetivo = 2 * C
capital_actual = C
años = 0

while capital_actual < capital_objetivo:
    capital_actual += capital_actual * interes_decimal
    años += 1

print(f"El capital se doblará al término de {años} años.")
print(f"Capital final: {capital_actual:.2f}")
