#  ejemplo del problema 2 en python 

#  lectura de datos
x = input("Por favor ingrese la variable X: ")
y = input("Por favor ingrese la variable Y: ")
z = input("Por favor ingrese la variable Z: ")
#  conversion de datos 
valorx = float (x)
valory = float (y)
valorz = float (z)
#  calculo de resultado
m = float((valorx+(valory/valorz))/(valorx-(valory/valorz)))
#  salida de datos
print ("El valor m, en base a las variables:\n x= %s\n\ty=%s\n\t\tz=%s" % (x,y,z))
print ("da como resultado \n\t\tm=%.2f\n" % m)