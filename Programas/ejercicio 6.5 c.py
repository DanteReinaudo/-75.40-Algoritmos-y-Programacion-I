def Ingreso():
    cadena=str(input("Ingrese una cadena: "))
    lista=cadena.split(" ")
    return(lista)
def busca_letra(cadena):
    for i in range (0,len(cadena)):
        if cadena[i][0]=="a" or cadena[i][0]=="A":
            print(cadena[i],end=" ")
chain=Ingreso()
busca_letra(chain)
