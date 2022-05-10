def Ingreso():
    cadena=input("Ingrese una cadena: ").lower() 
    return(cadena)
def cambia_vocal(cadena):
    nuevacadena=""
    for i in range (0,len(cadena)):
        if  cadena[i]!= "a" and cadena[i]!= "e" and cadena[i]!= "i" and cadena[i]!= "o" and cadena[i]!= "u":
            nuevacadena=nuevacadena + cadena[i]
        elif cadena[i]=="a":
            nuevacadena=nuevacadena + "e"
        elif cadena[i]=="e":
            nuevacadena=nuevacadena+"i"
        elif cadena[i]=="i":
            nuevacadena=nuevacadena+ "o"
        elif cadena[i]=="o":
            nuevacadena=nuevacadena+"u"
        elif cadena[i]=="u":
            nuevacadena=nuevacadena+"a"
    return(nuevacadena)
chain=Ingreso()
newchain=cambia_vocal(chain)
print(newchain)

