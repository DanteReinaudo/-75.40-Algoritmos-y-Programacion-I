print("Este programa le pide una cantidad de numeros y le calcula su factorial")
cantidad = int(input("Ingrese la cantidad de numeros que quiere ingresar: "))
for i in range (1,cantidad+1):
    num = int(input("Ingrese un numero: "))
    for j in range (num+1):
        factorial = 1
        for x in range (1,j+1):
            factorial = factorial*x
    print("El factorial", i ,"de", num ,"es", factorial)