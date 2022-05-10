n = int(input("Ingrese la cantidad de numeros que tendra su dominó: "))
for i in range (0,n+1):
    for j in range (0,n+1):
        if i >= j:
            print (i,"/",j)