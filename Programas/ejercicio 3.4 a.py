def Coordenadas():
    x=float(input("Ingrese la coordenada en el eje x del vector: "))
    y=float(input("Ingrese la coordenada en el eje y del vector: "))
    z=float(input("Ingrese la coordenada en el eje z del vector: "))
    return(x,y,z)
def calculaNorma(x,y,z):
    modulo=(x**2+y**2+z**2)**(1/2)
    return(modulo)
print("Ingrese un vector y el programa calcula su modulo")
x,y,z=Coordenadas()
norma=calculaModulo(x,y,z)
print("El modulo del vector ingresado (",x,",",y,",",z,") es", norma) 