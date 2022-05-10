#~linea.rstrip("n") borra caracteres
def Abrir():
    archivo=open("Ejercicio 10.1.txt")
    expresion=input("Ingrese una expresion: ")
    lista=[]
    for linea in archivo:
        linea=linea.rstrip("\n")
        lista.append(linea)
    for i in range(0,len(lista)):
        if expresion in lista[i]:
            print(lista[i])
    print(lista)
    
    
    
    
    archivo.close()
Abrir()