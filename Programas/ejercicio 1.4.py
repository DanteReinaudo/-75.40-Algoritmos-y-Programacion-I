n = int(input("Ingrese el numero al cual quiere calcularle su factorial: "))
for i in range (n+1):
    factorial = 1
    for y in range (1,i+1):
        factorial=factorial*y
print("El factorial de", n ,"es", factorial)
    
    