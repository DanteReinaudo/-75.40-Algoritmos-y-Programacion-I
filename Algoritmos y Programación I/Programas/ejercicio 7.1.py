def OrdenaTupla():
    tupla=[]
    dato=input("Ingrese un valor a la tupla, ingrese 0 para dejar de añadir: ")
    while dato !="0":
        tupla.append(dato)
        dato=input("Ingrese un valor a la tupla, ingrese 0 para dejar de añadir: ")
    tupla=tuple(tupla)
    tuplaprima=tupla[:]
    print(tuplaprima)
    print(tupla)
    sorted(tupla)
    print(tupla)
    if tuplaprima==tupla:
        print("La tupla esta ordenada de menor a mayor")
    elif tuplaprima!=tupla:
        print("La tupla no esta ordenada de menor a mayor")
OrdenaTupla()