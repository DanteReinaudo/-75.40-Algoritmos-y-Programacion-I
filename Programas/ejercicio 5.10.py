def Ingreso():
    num=int(input("Ingrese un numero:" ))
    return(num)
def BuscaPrimos(num):
    for i in range (1,num):
        a=0
        for j in range (1,i+1):
            if i % j == 0:
                a=a+1
        if a == 2:
            print("El numero", i ,"es primo")
        
numero=Ingreso()
BuscaPrimos(numero)
        