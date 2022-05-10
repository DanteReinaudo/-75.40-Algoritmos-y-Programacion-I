print("Este programa le pide notas y calcula su promedio, si desea dejar de ingresar notas ingrese un numero negativo")
nota = int(input("Ingrese una nota: "))
cantnota = 0
suma = 0 
while nota >= 0:
    suma = suma + nota
    cantnota += 1
    nota = float(input("Ingrese una nota: "))
if cantnota == 0:
    print("No hay notas ingresadas")
else:
    promedio = suma / cantnota
    print("El promedio de las notas ingresadas es", promedio)