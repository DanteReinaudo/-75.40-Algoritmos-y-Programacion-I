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
if mes == 4 or mes == 6 or mes == 9 or mes == 11 :
        if dia > 30:
            print("La fecha no es valida")
if mes == 2 and bisiesto == True:
        if dia > 29:
            print("La fecha no es valida")
if mes == 2 and bisiesto == False:
        if dia > 28:
            print("La fecha no es valida")
else:
    if mes == 12:
        faltan = 31 - dia
    if mes == 11:
        faltan = (30 - dia) + 31
    if mes == 10:
        faltan = ( 31 - dia ) + 31 + 30
    if mes == 9:
        faltan = ( 30 - dia ) + 31 + 30 + 31
    if mes == 8:
        faltan = ( 31 - dia ) + 31 + 30 + 31 + 30
    if mes == 7:
        faltan = ( 31 - dia ) + 31 + 30 + 31 + 30 + 31
    if mes == 6:
        faltan = ( 30 - dia ) + 31 + 30 + 31 + 30 + 31 + 31
    if mes == 5:
        faltan = ( 31 - dia ) + 31 + 30 + 31 + 30 + 31 + 31 + 30
    if mes == 4:
        faltan = ( 30 - dia ) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
    if mes == 3:
        faltan = ( 31 - dia ) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
    if mes == 2 :
        if bisiesto == True:
            faltan = ( 29 - dia ) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        if bisiesto == False:
            faltan = ( 28 - dia ) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
    if mes == 1 :
        if bisiesto == True:
            faltan = ( 31 - dia ) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 29
        if bisiesto == False:
            faltan = ( 31 - dia ) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28
print("Faltan", faltan ,"dias para que termine el año", año ,"desde la fecha ingresada")
if bisiesto == True:
    pasaron = 366 - faltan
if bisiesto == False:
    pasaron = 365 - faltan
print("Pasaron", pasaron ,"dias desdes el comienzo del año", año)
    