def Abrir():
    archivo=open("Ejercicio 10.1.txt")
    nuevoarchivo=open("Ejercicio 10.2.txt","w")
    for linea in archivo:
        nuevoarchivo.write(linea)
    archivo.close()
    nuevoarchivo.close()
Abrir()
        
        
    