def Ingreso():
    num=int(input("Ingrese un numero entero: "))
    return(num)
def FactoresPrimos(num):
    x = 2
    print("La descomposicion en facotres primos es : ")
    while num != 1:
        if num % x == 0:
            print(str(x) + " ")
            num = num / x
        else:
            x=x+1
num = Ingreso()
FactoresPrimos(num)
