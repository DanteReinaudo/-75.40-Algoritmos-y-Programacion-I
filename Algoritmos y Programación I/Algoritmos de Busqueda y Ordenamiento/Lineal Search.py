# -*- coding: utf-8 -*-
"""
Orden 1, mejor para tamaños de datos no muy grandes 
Es de orden constante si encuentra el objetivo en el primer lugar buscado (mejor caso posible)

"""

def linealSearch(item,lista):
    i=0
    found= False
    while i < len(lista) and found == False:
        if lista[i] == item:
            found=True
        else:
            i+=1
    return found,i
                
lista=[1,2,3,4,5,6]
item=54
found,lugar=linealSearch(item,lista)

if found:
    print("Se encontro ",item," en la posicion", lugar )
else:
    print("No se encontro")