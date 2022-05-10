# -*- coding: utf-8 -*-
"""
    Este algoritmo es poco eficiente y tiene orden 2,
    Es un dolbe ciclo for, en el primero busca cada una delas partes de la lista
    en el segundo,  compara si el numero es mayo al siguiente, si es asi lo intercambia del lugar,
    una vez realizo el primer ciclo, el mas grande llego al final, por lo que la busqueda se achica un espacio
    ya que no debe comparar el ultimo, por eso el "-i" en el segundo for
"""

lista=[100,26,102,22,12,5,41,9]
listaCopia=lista[:]
for i in range(len(listaCopia)):
    print()
    for j in range(0,len(listaCopia)-1-i):
        if listaCopia[j]>listaCopia[j+1]:
            listaCopia[j],listaCopia[j+1]=listaCopia[j+1],listaCopia[j]
            #puedo usar auxiliar
        print(listaCopia)

# print(listaCopia)
# print(sorted(lista))