def Ingreso():
    cadena=input("Ingrese una cadena de caracteres: ")
    list(cadena)
    return(cadena)
def separar(cadena):
    for i in range(0,len(cadena)):
        if cadena[i]!=" ":
            print(cadena[i],end="")
        elif cadena[i]==" ":
            print("_",end="")
        if i == len(cadena)-1:
            print(".txt")
chain=Ingreso()
separar(chain)