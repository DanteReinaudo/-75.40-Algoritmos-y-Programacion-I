print("Ingrese una fecha en formato (dia/mes/año)")
año = int(input("Ingrese un año: "))
mes = int(input("Ingrese un mes: "))
dia = int(input("Ingrese un dia: "))
if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
    bisiesto = True
else:
    bisiesto = False
if mes > 12  or mes < 1 or dia > 31 or dia < 1:
    print("La fecha ingresada no es valida.")
else:
    if mes == 4 or mes == 6 or mes == 9 or mes == 11 :
        if dia < 31:
            print("La fecha ingresada", dia,"/",mes,"/",año ,"es valida")
        else:
            print("La fecha ingresada no es valida")
    elif mes == 2 and bisiesto == True:
        if dia < 30 :
            print("La fecha ingresada", dia,"/",mes,"/",año ,"es valida")
        else:
            print("La fecha ingresada no es valida")
    elif mes == 2 and bisiesto == False:
        if dia < 29:
            print("La fecha ingresada", dia,"/",mes,"/",año ,"es valida")
        else:
            print("La fecha ingresada no es valida")
    else:
        print("La fecha ingresada", dia,"/",mes,"/",año ,"es valida")
    