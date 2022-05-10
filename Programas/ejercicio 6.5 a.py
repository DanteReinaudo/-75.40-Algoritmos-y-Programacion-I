def Ingreso():
    cadena=str(input("Ingrese una cadena: ")).upper()
    
    return(cadena)
def Iniciales(cadena):
    print(cadena[0],end="")
    for i in range (0,len(cadena)):
        if cadena[i] == " ":
            print(cadena[i+1],end="")

cadena=Ingreso()
Iniciales(cadena)
 