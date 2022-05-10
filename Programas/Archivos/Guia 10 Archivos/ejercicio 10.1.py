def Head (nombrearchivo):
    archivo=open(nombrearchivo,"r")
    lineasTotales=0
    for linea in archivo:
        lineasTotales=lineasTotales+1
    bandera=False
    while bandera==False:
        try:
            n=int(input("Ingrese un numero entero para el intervalo de lineas del archivo que desea imprimir: "))
            if n < 0 or n > lineasTotales:
                print("El archivo no tiene ese numero de lineas")
            else:
                bandera=True
        except:
            print("Eso no es un entero.")
    archivo=open(nombrearchivo,"r")
    nroLinea=1
    while nroLinea<=n:
        linea=archivo.readline()
        linea.rstrip("\n")
        print(linea)
        nroLinea=nroLinea+1
    
    archivo.close()

Head("ejercicio 10.1.txt")
