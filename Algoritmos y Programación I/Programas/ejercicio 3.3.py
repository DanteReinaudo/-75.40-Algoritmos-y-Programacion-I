def ingresoNumeros(orden):
    num=float(input("Ingrese el {0} numero: ".format(orden)))
    return(num)
def Multiplicacion(a,b):
    total=a*b
    return(total)
def comparaMaximos(p1,p2,p3,p4,p5,p6):
    lista=[p1,p2,p3,p4,p5,p6]
    maximo=-9999999999999999
    for i in lista:
        if i > maximo:
            maximo = i
    return(maximo)
print("El programa le pide 4 numeros y le dice cual es la mayor multiplicacion entre ellos")
num1=ingresoNumeros("primer")
num2=ingresoNumeros("segundo")
num3=ingresoNumeros("tercer")
num4=ingresoNumeros("cuarto")
producto12=Multiplicacion(num1,num2)
producto13=Multiplicacion(num1,num3)
producto14=Multiplicacion(num1,num4)
producto23=Multiplicacion(num2,num3)
producto24=Multiplicacion(num3,num4)
producto34=Multiplicacion(num3,num4)
elmasgrande=comparaMaximos(producto12,producto13,producto14,producto23,producto24,producto34)
print("El producto mas grande es", elmasgrande)