# -*- coding: utf-8 -*-
"""
Mas eficiente que la busqueda burbuja
Necesita que la lista este ordenada !
Parte a la mitad la lista, compara si el del medio es el que busca,
sino lo es compara si mi item buscado es mayor o menor al del medio
descarta la parte que no corresponda, y vuelve a hacer lo mismo con la mitad
correcta, parte la mitad a la mitad y asi.
"""
def binarySeach(item,lista):
    found=False
    first=0 #Izquierda
    last= len(lista)-1 #Derecha
    while first<=last and found==False:
        medio=(first+last)//2
        if lista[medio]==item:
            found=True
        else:
            if lista[medio]<item:
                first=medio+1
            elif lista[medio]>item:
                last=medio-1
        return found
                