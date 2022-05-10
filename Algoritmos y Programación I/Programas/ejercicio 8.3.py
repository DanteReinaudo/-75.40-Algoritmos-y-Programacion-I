def agenda(lista,parametro):
    listaAparece=[]
    for i in range (0,len(lista)):
        if parametro in lista[i][0]:
            listaAparece.append(lista[i])
    print(listaAparece)
lista=[("juan domingo",420),("alberto",178),("juanfer quintero",10),("kokiflow",100)]            
agenda(lista,"juan")