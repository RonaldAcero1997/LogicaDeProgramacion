nombre = input ("Ingrese el nombre del estudiante:")
programa = input ("Ingrese el nombre del Programa de Estudios al que postula:")
promedio = float (input ("Ingrese el promedio obtenido en el examen de admision (0-20):"))

if promedio >= 17:
    estado = "Beca"
    matricula = 0.00
    #print("Estado de beca: EXCELENCIA.")
   # print("El monto a pagar es de: S/0.00")
elif promedio >=13 and promedio <= 16.9:
    estado = "Regular"
    matricula = 150.00
    #print("Estado de beca: REGULAR.")
    #print("El monto a pagar es de: S/150.00.")
elif promedio < 13:
    estado = "Espera"
    matricula = 0.00
     #print("Estado de beca: EN ESPERA.")
    # print("No se le cobra matricula.")
else:
    print("ERROR: No el valor correcto.")

print("\n ---TICKET DE RESPUESTA ---")
print(f"Estudiante: {nombre}")
print(f"Programa de Estudio: {programa}")
print(f"Estado: {estado}")
print(f"Monto a pagar: {matricula}")
print("-----------------------------")