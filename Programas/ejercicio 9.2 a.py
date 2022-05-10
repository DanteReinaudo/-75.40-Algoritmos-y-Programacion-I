def CHAIN():
    cadena=input("Ingrese una cadena: ")
    return(cadena)
def Cuenta_Palabras(chain):
    cadena=chain.split()
    print(cadena)
    frecuencia=[]
    for i in cadena:
        frecuencia.append(cadena.count(i))
    print(frecuencia)
    dic=dict(zip(cadena,frecuencia))
    print(dic)

cadena=CHAIN()
Cuenta_Palabras(cadena)