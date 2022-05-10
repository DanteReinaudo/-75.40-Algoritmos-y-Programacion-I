def Ingreso_Nombre():
    lista=[]
    nombre=input("Ingrese su nombre, ingrese 0 si no desea imgresarlo: ")
    while nombre!="0":
        lista.append(nombre)
        nombre=input("Ingrese su nombre, ingrese 0 si no desea imgresarlo: ")
    tupla=tuple(lista)
    p=int(input("Ingrese una posicion: "))
    n=int(input("Ingrese una cantidad de nombres: "))
    return(tupla,p,n)
def VotoLoco(tupla,p,n):
    if p < len(tupla):
        if (p+n)<=len(tupla):
            for i in range(p,p+n):
                print("Querido", tupla[i] ,"vote por mi, Dante, siempre con vos")
        elif (p+n)>len(tupla):
            for i in range(p,len(tupla)):
                print("Querido", tupla[i] ,"vote por mi, Dante, siempre con vos")
    
neopistea,peron,jesus=Ingreso_Nombre()
VotoLoco(neopistea,peron,jesus)