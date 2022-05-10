def Ingreso():
    cantidad=int(input("Ingrese una cantidad: "))
    return(cantidad)
def Abrir():
    archivo=open("Ejercicio 10.1.txt")
    return(archivo)
def Leer(file,cantidad):
    for i in range(0,cantidad):
        linea=archivo.readline()
        print(linea)
def Cerrar(file):
    file.close()
cantidad=Ingreso()
archivo=Abrir()
Leer(archivo,cantidad)
Cerrar(archivo)
