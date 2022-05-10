def validarEnteros(mensaje):
    bandera=True
    while bandera:
        try:
            entero=int(input(mensaje))
            bandera=False
        except ValueError:
            print("La opcion ingresada no es valida.")
    return(entero)
num=validarEnteros('A qué playlist quiere añadir canciones?(Nro): ')
print(num)