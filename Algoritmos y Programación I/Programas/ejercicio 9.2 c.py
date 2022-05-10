from random import randint
def Tirada():
    cantidad=randint(1,10)
    print(cantidad)
    listadados=[]
    listasuma=[]
    for i in range(cantidad):
        a=randint(1,6)
        b=randint(1,6)
        suma=a+b
        listasuma.append(suma)
        tupla=(a,b)
        listadados.append(tupla)
    print(listadados)
    print(listasuma)
    return(listadados,listasuma)
def Frecuencia(listadados,listasuma):
    frecuencia=[]
    for numero in listasuma:
        frecuencia.append(listasuma.count(numero))
    print(frecuencia)
    dicc=dict(zip(listasuma,frecuencia))
    print(dicc)
listadados,listasuma=Tirada()
Frecuencia(listadados,listasuma)