print("Bienvenido, este programa solicita dos numeros y le devuelve la suma, la division, la resta y la multiplicacion entre ambos")
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
suma = n1 + n2
resta12 = n1 - n2
resta21 = n2 - n1
multiplicacion = n1*n2
division12 = n1/n2
division21 = n2/n1
print("La suma entre", n1 ,"y", n2 ,"es", suma)
print("La resta entre", n1 ,"y", n2 ,"es", resta12)
print("La resta entre", n2 ,"y", n1 ,"es", resta21)
print("La multiplicacion entre", n1 ,"y", n2 ,"es", multiplicacion)
print("La division entre", n1 ,"y", n2 ,"es", division12)
print("La division entre", n2 ,"y", n1 ,"es", division21)