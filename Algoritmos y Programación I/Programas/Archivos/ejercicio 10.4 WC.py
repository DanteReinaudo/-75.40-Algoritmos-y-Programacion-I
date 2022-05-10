def Abrir():
    archivo=open("Ejercicio 10.1.txt")
    cantlineas=0
    cantpalabras=0
    cantcaracteres=0
    for linea in archivo:
        cantlineas=cantlineas+1
        lineas=linea.split()
#        print(lineas)
        cantpalabras=cantpalabras+len(lineas)
        Linea=list(linea)
        cantcaracteres=cantcaracteres+len(Linea)
#        print(Linea)
    print("El archivo tiene", cantlineas ,"lineas")
    print("El archivo tiene", cantpalabras ,"palabras")
    print("El archivo tiene", cantcaracteres ,"caracteres")
    archivo.close()
Abrir()