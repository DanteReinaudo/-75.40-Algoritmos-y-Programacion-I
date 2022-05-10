def Ingreso():
    numero=input("Ingrese un numero: ")
    return(numero)
def separar(numero):
    contador=-3
    nuevacadena=[""]
    for i in range (-1,-len(numero)-1,-1):
        nuevacadena=nuevacadena.append(numero[i])
        if i==contador and i!=-len(numero):
            nuevacadena=nuevacadena.append(".")
            contador=contador-3
    for i in range (-1,len(nuevacadena)-1,-1):
        print(nuevacadena[i])
numero=Ingreso()
separar(numero)