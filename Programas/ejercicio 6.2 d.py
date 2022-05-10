def Ingreso():
    cadena=input("Ingrese una cadena: ")
    return(cadena)
def code(cadena):
    contador=2
    for i in range(0,len(cadena)):
        print(cadena[i],end="")
        if i == contador:
            print(".",end="")
            contador=contador+3
cadena=Ingreso()
code(cadena)