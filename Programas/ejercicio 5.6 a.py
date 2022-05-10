def Ingreso():
    num = int(input("Ingrese un numero entero positivo: "))
    return(num)
def Potencia_de_Dos(num):
    potencia=2
    cantidad=1
    while potencia < num:
        potencia=potencia*2
        cantidad+=1
    if potencia == num:
        estado= True
    elif potencia != num:
        estado = False
    return(estado,cantidad)



num = Ingreso()
estado,cantidad = Potencia_de_Dos(num)
if estado == True:
    print("El numero", num ,"es potencia", cantidad ,"de dos")
elif estado == False:
    print("El numero", num ," no es potencia de dos")