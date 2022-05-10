def puntoA(lista,parametro):
    total=0
    for i in range (0,len(lista)):
        if lista[i]==parametro:
            total=total+1
    return(total)

def puntoB(lista,parametro):
    primeraposicion="no esta"
    nro=0
    while lista[nro] != parametro and nro < len(lista)-1:
        nro=nro+1
    if lista[nro] == parametro:
        primeraposicion=nro
    return(primeraposicion)

def puntoC(lista,parametro):
    posiciones=[]
    for i in range (0,len(lista)):
        if lista[i]==parametro:
            posiciones.append(i)
    return(posiciones)
            
total=puntoA([1,2,3],3)
print(total)
total2=puntoA([1,2,3],4)
print(total2)
ubicacion=puntoB([1,2,3],3)
print(ubicacion)
ubicacion2=puntoB([1,2,3],0)
print(ubicacion2)
ubicaciones=puntoC([1,1,1],1)
print(ubicaciones)
            