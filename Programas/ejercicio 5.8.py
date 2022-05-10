print("Este programa le solicita una sucesion de numeros y le calcula el promedio, para dejar de ingresar, ingrese -1")
num=int(input("Ingrese un numero entero: "))
cantidad = 0
suma = 0
while num != -1:
    cantidad += 1
    suma = suma + num
    num = int(input("Ingrese un numero entero: "))
promedio = suma/cantidad
print("Fueron ingresados un total de", cantidad ,"numeros")
print("La suma total es", suma)
print("El promedio de todos los numeros es", promedio)