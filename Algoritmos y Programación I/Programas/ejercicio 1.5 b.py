print("Este programa le solicita un numero y le devuelve su tabla de multiplicar del 1 al 10")
n = int(input("Ingrese el numero cuya tabla quiere obtener: "))
print("Su tabla es: ")
for i in range (1,11):
    a = n*i
    print(n ,"por", i ,"es" ,a)