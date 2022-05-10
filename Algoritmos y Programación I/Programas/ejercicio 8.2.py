def ordenando(lista):
    valormax=lista[0]
    for i in range(0,len(lista)):
        if lista[i]>valormax:
            valormax=lista[i]
            posicion=i
    tupla=(valormax,posicion)
    return(tupla)
tupla=ordenando(["a","v","d","e","f","g"])
print(tupla)
tupla2=ordenando([1,2,10,5])
print(tupla2)