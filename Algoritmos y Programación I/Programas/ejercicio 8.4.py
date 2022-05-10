def factura(listaprecio,listacompra):
    preciototal=0
    compratotal=[]
    for i in range (0,len(listacompra)):
        compra=[]
        for j in range(0,len(listaprecio)):
            if listacompra[i][0] == listaprecio[j][0]:
                compra.append(listacompra[i][1])
                compra.append(listaprecio[j][1])
                compra.append(listaprecio[j][2])
                precio=listaprecio[j][2]*listacompra[i][1]
                compra.append(precio)
        preciototal=preciototal+precio
        compratotal.append(compra)
    compratotal.append(preciototal)
    for i in range (0,len(compratotal)):
        print(compratotal[i])
        
lista1=[("Leche","rica leche 420",50),("Birra","rica birra 420", 100),("Base","rica base del doctor",420),("Agua","clave",1)]
lista2=[("Leche",10),("Base",5),("Birra",20)]
factura(lista1,lista2)
#tuplaidentidad=(identificador,descricpion,precio)
#tuplacompras=(identificador,cantidad)
#factura: cantidad, descripcion, precio unitario, precio total de la unidad, preci ototal de compras