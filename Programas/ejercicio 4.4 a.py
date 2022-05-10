print("El programa calcula el  maximo y el minimo de una funcion cuadratica: ")
print("La funcion debe estar expresada de la forma y = a*x*x + b*x + c")
a = float(input("Ingrese el termino que acompaña al x al cuadrado: "))
while a == 0:
    print("El numero no puede ser 0")
    a = float(input("Ingrese el termino que acompaña al x al cuadrado: "))
b = float(input("Ingrese el termino que acompaña a x: "))
c = float(input("Ingrese el termino independiente: "))
vertice = -b/(2*a)
y = a*vertice*vertice + b*vertice + c
if a > 0 :
    print("El minimo de la funcion se halla en el punto(",vertice,",",y,")")
elif a < 0:
    print("El maximo de la funcion se halla en el punto (",vertice,",",y,")")
