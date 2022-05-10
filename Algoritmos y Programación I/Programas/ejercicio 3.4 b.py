def Coordenadas(orden):
    x=float(input("Ingrese la coordenada en el eje x del {0} vector: ".format(orden)))
    y=float(input("Ingrese la coordenada en el eje y del {0} vector: ".format(orden)))
    z=float(input("Ingrese la coordenada en el eje z del {0} vector: ".format(orden)))
    return(x,y,z)
def diferencia(a,b):
    resta= a-b
    return(resta)
print("Este programa le pide dos vectores y le devuelve la resta entre el primero y el segundo.")
x1,y1,z1=Coordenadas("primer")
x2,y2,z2=Coordenadas("segundo")
x=diferencia(x1,x2)
y=diferencia(y1,y2)
z=diferencia(z1,z2)
print("La diferencia entre los vectores es (", x ,",", y ,",", z ,")")