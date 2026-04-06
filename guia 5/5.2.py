mes = input("Introduce el nombre del mes: ").strip().lower()
es_bisiesto = input("¿El año es bisiesto? (si/no): ").strip().lower()

dias = 0

if mes in ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]:
    dias = 31
elif mes in ["abril", "junio", "septiembre", "noviembre"]:
    dias = 30
elif mes == "febrero":
    if es_bisiesto == "si":
        dias = 29
    else:
        dias = 28
else:
    print("Mes no válido.")

if dias > 0:
    print(f"El mes de {mes} tiene {dias} días.")
