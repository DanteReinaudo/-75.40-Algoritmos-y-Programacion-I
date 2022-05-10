def Ingreso():
    clave=input("Ingrese una clave: ")
    return(clave)
def cripteo(clave):
    print("Su clave es:", len(clave)*"X")
clave=Ingreso()
cripteo(clave)
