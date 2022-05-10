def Cargar_Datos():
    archivo=open("Ejercicio 10.7 a.txt")
    nombres=[]
    club=[]
    for linea in archivo:
        linea=linea.rstrip("\n")
        linea=linea.split(",")
#        print(linea)
        nombres.append(linea[0])
        club.append(linea[1])
    diccionario=dict(zip(nombres,club))
    print(diccionario)
        
        
    archivo.close()
Cargar_Datos()