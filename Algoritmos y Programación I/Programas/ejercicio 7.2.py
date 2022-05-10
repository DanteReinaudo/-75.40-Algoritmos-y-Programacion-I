def Ingreso_Tupla(Orden):
    tupla=[]
    dato1=int(input("Ingrese el primer valor de la {0} ficha: ".format(Orden)))
    dato2=int(input("Ingrese el segundo valor de la {0} ficha: ".format(Orden)))
    tupla.append(dato1)
    tupla.append(dato2)
    tupla=tuple(tupla)
    return(tupla)
def Ingreso_CHAIN(orden):
    tupla=input("Ingrese la ficha de domino separada por un espacio: ")
    peron=tupla.split()
    print(peron)
    return(peron)
def Domino(ficha1,ficha2):
    contador=0
    for i in (0,1):
        for j in (0,1):
            if ficha1[i]==ficha2[j]:
                print("Las fichas encajan dado que", ficha1[i] ,"encaja con", ficha2[j])
                contador=+1
    if contador==0:
        print("Las fichas no encajan")
#ficha1=Ingreso_Tupla("primer")
#ficha2=Ingreso_Tupla("segunda")
#Domino(ficha1,ficha2)
ficha3=Ingreso_CHAIN("primer")
ficha4=Ingreso_CHAIN("segunda")
Domino(ficha3,ficha4)