def Ingreso_Nombre():
    lista=[]
    nombre=input("Ingrese su nombre, ingrese 0 si no desea imgresarlo: ")
    while nombre!="0":
        lista.append(nombre)
        nombre=input("Ingrese su nombre, ingrese 0 si no desea imgresarlo: ")
    tupla=tuple(lista)
    return(tupla)
def VotoLoco(tupla):
    for i in range(0,len(tupla)):
        print("Querido", tupla[i] ,"vote por mi, Dante, siempre con vos")
neopistea=Ingreso_Nombre()
VotoLoco(neopistea)