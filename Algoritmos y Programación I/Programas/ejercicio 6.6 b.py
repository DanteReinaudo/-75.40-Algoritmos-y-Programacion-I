def Ingreso():
    cadena=input("Ingrese una cadena: ").lower() 
    return(cadena)
def quita_consonantes(cadena):
    for i in range(0,len(cadena)):
        if  cadena[i] == "a" or cadena[i] == "e" or cadena[i] == "i" or cadena[i] == "o" or cadena[i]== "u":
            print(cadena[i],end="")
chain=Ingreso()
quita_consonantes(chain)