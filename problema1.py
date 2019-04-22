# ejemplo del problema1 en pyhton

#  entrada de datos
hora = input("Por favor ingrese el numero de horas: ")
costo = input("Por favor ingrese el costo por hora: ")

#  calculo de datos
sueldo = float(int(costo) * int(hora))
descuento = float(sueldo * 0.10)
total = float(sueldo - descuento)

#  salida de datos

print("Su descuento del seguro social es de: %.2f$\n" % descuento)
print ("El sueldo mensual del trabajador es: %.2f$\n"% total)