def Ingreso ():
    num = int(input("Ingrese un numero entero: "))
    return(num)
def suma_divisor(num):
    suma=0
    for i in range (1,num):
        if num%i== 0:
            print(i ,"es divisor")
            suma=suma+i
    return(suma)