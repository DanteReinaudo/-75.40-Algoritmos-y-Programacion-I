año = int(input("Ingrese un año: "))
if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
    print("El año", año ,"es bisiesto")
    dosnueve = True
else:
    print("El año", año ,"no es bisiesto")
mes = input("Ingrese un mes del año: ")
if mes == str("abril") or mes == str("junio") or mes == ("septiembre") or mes == str("noviembre"):
    print("El mes", mes ,"tiene 30 dias")
elif mes == str("enero") or mes == str("marzo") or mes == ("mayo") or mes == str("julio") or mes == str("agosto") or mes == str("octubre") or mes == str("diciembre"):
    print("El mes", mes ,"tiene 31 dias")
elif mes == str("febrero"):
    if dosnueve == True:
        print("El mes", mes ,"tiene 29 dias")
    else:
        print("El mes", mes ,"tiene 28 dias")
else:
    print("El mes ingresado no es valido.")   