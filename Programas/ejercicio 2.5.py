print("Este programa le pide un numero n y devuelve los primeros n numeros triangulares")
n = int(input("Ingrese un numero entero n: "))
for i in range (1,n+1):
    triangular = i*(i+1)/2
    print(i,"-",int(triangular))
