def Ingreso(orden):
    num = int(input("Ingrese el {0} numero entero positivo: ".format(orden)))
    return(num)
def suma_divisor(num):
    suma=0
    for i in range (1,num):
        if num%i== 0:
            print(i ,"es divisor de", num)
            suma=suma+i
    print("La suma total de los divisores de", num ,"es:", suma)
    return(suma)
num1=Ingreso("primer")
num2=Ingreso("segundo")
sumadivisor1=suma_divisor(num1)
sumadivisor2=suma_divisor(num2)
if sumadivisor1==num2 and sumadivisor2==num1:
    print("El numero", num1 ,"y el numero", num2,"son numeros amigos")
    if num1==num2:
        print("Ademas es un numero perfecto")
else:
    print("El numero", num1 ,"y el numero", num2,"no son numeros amigos")

    
    