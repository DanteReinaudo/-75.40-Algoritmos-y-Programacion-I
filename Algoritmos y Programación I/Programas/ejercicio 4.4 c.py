m1 = float(input("Ingrese la pendiente de la primer recta: "))
b1 = float(input("Ingrese la ordenada al origen de la primer recta: "))
m2 = float(input("Ingrese la pendiente de la segunda recta: "))
b2 = float(input("Ingrese la ordenada al origen de la segunda recta: "))
if m1 == m2 and b1 == b2:
    print("Las rectas son iguales intersectan en sus infinitos puntos")
elif m1 == m2 and b1 != b2:
    print("Las rectas son paralelas, se intersectan en el infinito.")
elif m1 != m2:
    x = (b2 - b1)/(m1 - m2)
    y = m1*x + b1
    print("Las rectas se intersectan en el punto: (",x,",",y,")")