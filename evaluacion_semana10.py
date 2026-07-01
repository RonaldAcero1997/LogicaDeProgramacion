print("==========================================================")
print("  MÓDULO DE SELECCIÓN AUTOMÁTICA DE BECAS DE POSTULANTES")
print("==========================================================")

nombre = input("Ingrese su nombre completo: ")
programa = input("Ingrese su programa de estudios: ")

while True:
    try:
        promedio = float(input("Ingrese su promedio de admisión (0 - 20): "))

        if promedio < 0 or promedio > 20:
            print("Error: El promedio debe estar entre 0 y 20.")
        else:
            break
    except ValueError:
        print("Error: Debe ingresar un número válido.")

while True:
    try:
        ingreso = float(input("Ingrese el ingreso familiar mensual (S/): "))

        if ingreso < 0:
            print("Error: El ingreso no puede ser negativo.")
        else:
            break
    except ValueError:
        print("Error: Debe ingresar un número válido.")

if promedio >= 17 and ingreso <= 1200:
    estado = "Beca de Excelencia"
    matricula = 0.00

elif promedio >= 13 and ingreso <= 2500:
    estado = "Beca Parcial"
    matricula = 75.00

elif promedio >= 13:
    estado = "Admitido Regular"
    matricula = 150.00

else:
    estado = "Lista de Espera"
    matricula = 0.00

print("\n==========================================")
print("      TICKET DE EVALUACIÓN")
print("==========================================")
print(f"Nombre               : {nombre}")
print(f"Programa de Estudios : {programa}")
print(f"Estado               : {estado}")
print(f"Monto                : {matricula}")
print(f"=========================================")