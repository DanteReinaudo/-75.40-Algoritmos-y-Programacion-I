def Ingreso():
    lista1=[]
    lista2=[]
    opcion="SI"
    while opcion!="NO":
        dato1=input("Ingrese el primer valor de la tupla: ")
        dato2=input("Ingrese el segundo valor de la tupla: ")
        lista1.append(dato1)
        lista2.append(dato2)
        opcion=input("Desea ingresar otro valor SI/NO?: ").upper()
    return(lista1,lista2)
def Dicc(lista1,lista2):
    diccionario=dict(zip(lista1,lista2))
    print(diccionario)
lista1,lista2=Ingreso()
Dicc(lista1,lista2)