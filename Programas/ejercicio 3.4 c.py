def Coordenadas(orden):
    x=float(input("Ingrese la coordenada en el eje x del {0} vector: ".format(orden)))
    y=float(input("Ingrese la coordenada en el eje y del {0} vector: ".format(orden)))
    z=float(input("Ingrese la coordenada en el eje z del {0} vector: ".format(orden)))
    return(x,y,z)
def productoVectorial(x1,y1,z1,x2,y2,z2):
    productox = y1*z2 - z1*y2
    productoy = z1*x2 - z2*x1
    productoz = x1*y2 - x2*y1
    return(productox,productoy,productoz)
print("Este programa le pide dos vectores y le devuelve el producto escalar v1 X v2.")
x1,y1,z1=Coordenadas("primer")
x2,y2,z2=Coordenadas("segundo")
pex,pey,pez= productoVectorial(x1,y1,z1,x2,y2,z2)
print("El producto vectorial entre el primero y el segundo es (", pex ,",", pey ,",", pez ,")")