print("El programa calcula las raices de una funcion cuadratica: ")
print("La funcion debe estar expresada de la forma y = a*x*x + b*x + c")
a = float(input("Ingrese el termino que acompaña al x al cuadrado: "))
while a == 0:
    print("El numero no puede ser 0")
    a = float(input("Ingrese el termino que acompaña al x al cuadrado: "))
b = float(input("Ingrese el termino que acompaña a x: "))
c = float(input("Ingrese el termino independiente: "))
radicando = b**2 - 4*a*c
if radicando < 0:
    print("La funcion tiene raices complejas")
else:
    raiz1 = (-b - (radicando**(1/2)))/(2*a)
    raiz2 = (-b + (radicando**(1/2)))/(2*a)
    print("Las raices de la funcion son", raiz1 ,"y", raiz2)
