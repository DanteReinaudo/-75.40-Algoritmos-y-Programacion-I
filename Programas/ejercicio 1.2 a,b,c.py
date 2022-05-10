X1 = int(input("Ingrese la primer coordenada sobre el eje x: "))
X2 = int(input("Ingrese la segunda coordenada sobre el eje x: "))
Y1 = int(input("Ingrese la primer coordenada sobre el eje y: "))
Y2 = int(input("Ingrese la segunda coordenada sobre el eje x: "))
if X1 > X2 :
    BASE = X1 - X2
elif X2 > X1 :
    BASE = X2 - X1
elif X1 == X2 :
    BASE = 0
if Y1 > Y2 :
    ALTURA = Y1 - Y2
elif Y2 > Y1 :
    ALTURA = Y2 - Y1
elif Y2 == Y1 :
    ALTURA = 0
PERIMETRO = BASE*2 + ALTURA*2
AREA = BASE*ALTURA
print("El perimetro del rectangulo es", PERIMETRO ,"el area es", AREA)