def Ingreso():
    cadena=input("Ingrese una cadena de caracteres: ")
    separador=input("Ingrese el caracter que quiere utilizar para separar la cadena: ")
    return(cadena,separador)
def separar(cadena,separador):
    for i in range(0,len(cadena)):
        if i < len(cadena) - 1:
            print(cadena[i],end="")
            print(separador,end="")
        if i == len(cadena)-1:
            print(cadena[i],end="")
chain,separador=Ingreso()
separar(chain,separador)