def Coordenadas(orden):
    x=float(input("Ingrese la coordenada en el eje x del {0} lado del triangulo: ".format(orden)))
    y=float(input("Ingrese la coordenada en el eje y del {0} lado del triangulo: ".format(orden)))
    z=float(input("Ingrese la coordenada en el eje z del {0} lado del triangulo: ".format(orden)))
    return(x,y,z)
def calculaNorma(x,y,z):
    modulo=(x**2+y**2+z**2)**(1/2)
    return(modulo)
def calculaArea(norma1,norma2,norma3):
    h = (norma1 + norma2 + norma3)/2
    area=(h*((h-norma1)*(h-norma2)*(h-norma3)))*(1/2)
    return(area)
x1,y1,z1=Coordenadas("primer")
x2,y2,z2=Coordenadas("segundo")
x3,y3,z3=Coordenadas("tercer")
norma1=calculaNorma(x1,y1,z1)
norma2=calculaNorma(x2,y2,z2)
norma3=calculaNorma(x3,y3,z3)
areatriangulo=calculaArea(norma1,norma2,norma3)
print("El area del triangulo es", areatriangulo)