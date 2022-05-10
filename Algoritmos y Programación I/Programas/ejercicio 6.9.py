def Ingreso():
    mensaje=input("Ingrese un mensaje: ")
    minimo=int(input("Ingrese el valor minimo: "))
    maximo=int(input("Ingrese el valor maximo: "))
    return(minimo,maximo,mensaje)
def pedir_entero(minimo,maximo,mensaje):
    print(mensaje ,"[",minimo,",",maximo,"] :")
    num=int(input())
    while num >= maximo or num < minimo:
        print("El numero ingresado no es valido.")
        print(mensaje ,"[",minimo,";",maximo,"] :")
        num=int(input())
minimo,maximo,mensaje=Ingreso()
pedir_entero(minimo,maximo,mensaje)