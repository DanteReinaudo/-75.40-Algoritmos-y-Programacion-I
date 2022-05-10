# -*- coding: utf-8 -*-
"""
Asume que el primer item esta ordenado, 
"""

# def insertionSort(lista):
#     for i in range(len(lista)):
#         print(lista)
#         for j in range(i,0,-1):
#             if lista[j-1]>lista[j]:
#                 aux=lista[j]
#                 lista[j]=lista[j-1]
#                 lista[j-1]=aux
#             print(lista)
#         print()
#     return(lista)
# lista=[420,100,3,7,4,20,5]
# listaOrdenada=insertionSort(lista)
# print(listaOrdenada)        

def insertionSort(lista):
    n=len(lista)
    for i in range(1,n):
        value=lista[i]
        j=i
        print(lista)
        while j>0 and lista[j-1]>value:
            lista[j]=lista[j-1]
            j=j-1
            print(lista)
        lista[j]=value
        print()
    return(lista)

lista=[420,100,3,7,4,20,5]
listaOrdenada=insertionSort(lista)
print(listaOrdenada)    