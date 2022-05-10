def Ingreso():
    cadena=input("Ingrese una cadena: ").lower() 
    return(cadena)
def quita_vocales(cadena):
    for i in range(0,len(cadena)):
        if  cadena[i]!= "a" and cadena[i]!= "e" and cadena[i]!= "i" and cadena[i]!= "o" and cadena[i]!= "u":
            print(cadena[i],end="")
chain=Ingreso()
quita_vocales(chain)