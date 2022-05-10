def Ingreso():
    cadena=input("Ingrese una cadena: ").lower()
    subcadena=input("Ingrese la subcadena que desea buscar en su cadena: ").lower()
    return(cadena,subcadena)
def busca_chain(cadena,subcadena):
    if subcadena in cadena:
        print("La subcadena", subcadena ,", esta dentro de la palabra", cadena)
    else:
        print("La subcadena", subcadena ,", no esta dentro de la palabra", cadena)
chain,subchain=Ingreso()
busca_chain(chain,subchain)