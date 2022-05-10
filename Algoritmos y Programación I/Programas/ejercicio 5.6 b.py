def Ingreso(orden):
    num = int(input("Ingrese el {0} numero entero positivo: ".format(orden)))
    return(num)
def Potencia_de_Dos(num):
    potencia=2
    while potencia < num:
        potencia=potencia*2
    if potencia == num:
        estado= True
    elif potencia != num:
        estado = False
    return(estado)
def Intervalo_Potencia (num1,num2):
    cantidad = 0
    total = 0
    for i in range (num1,num2):
        estado = Potencia_de_Dos(i)
        if estado == True:
            print(i ,"es potencia de 2")
            cantidad += 1
            total = total + i
    return(total, cantidad)

num1=Ingreso("primer")
num2=Ingreso("segundo")
sumatotal,cantidad = Intervalo_Potencia(num1,num2)
if cantidad == 1:
    print("Hay", cantidad ,"numero que es potencia de dos entre", num1 ,"y", num2 ,"y la suma de todos es", sumatotal)
else:
    print("Hay", cantidad ,"numeros que son potencia de dos entre", num1 ,"y", num2 ,"y la suma de todos es", sumatotal)
