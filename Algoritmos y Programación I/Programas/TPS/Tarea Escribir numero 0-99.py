#Este programa permite el ingreso de un numero entero entre 0 y 99 y muestra el resultado en letras
print("Bienvenido, ingrese un numero entre el 0 y el 99")
num = int(input("Ingrese un numero entero entre el 0 y el 99: "))
resto = num % 10
resultado = num // 10
if num > 99 or num < 0:
    print("El numero no se encuentra dentro del dominio del programa")
    num = int(input("Ingrese un numero entero entre el 0 y el 99: "))
#defino el 0
if resultado == 0 and resto == 0:
    nombre = "CERO"
#defino las unidades
if resto == 0:
    unidad = ""
elif resto == 1:
    unidad = "UNO"
elif resto == 2:
    unidad = "DOS"
elif resto == 3:
    unidad = "TRES"
elif resto == 4:
    unidad = "CUATRO"
elif resto == 5:
    unidad = "CINCO"
elif resto == 6:
    unidad = "SEIS"
elif resto == 7:
    unidad = "SIETE"
elif resto == 8:
    unidad = "OCHO"
elif resto == 9:
    unidad = "NUEVE"
#defino las decenas
if resultado == 0:
    decena = ""
elif resultado == 2:
    if resto == 0:
        decena = "VEINTE"
    else:
        decena = "VEINTI"
elif resultado == 3:
    if resto == 0:
        decena = "TREINTA"
    else:
        decena = "TREINTA Y "
elif resultado == 4:
    if resto == 0:
        decena = "CUARENTA"
    else:
        decena = "CUARENTA Y "
elif resultado == 5:
    if resto == 0:
        decena = "CINCUENTA"
    else:
        decena = "CINCUENTA Y "
elif resultado == 6:
    if resto == 0:
        decena = "SESENTA"
    else:
        decena = "SESENTA Y "
elif resultado == 7:
    if resto == 0:
        decena = "SETENTA"
    else:
        decena = "SETENTA Y "
elif resultado == 8:
    if resto == 0:
        decena = "OCHENTA"
    else:
        decena = "OCHENTA Y "
elif resultado == 9:
    if resto == 0:
        decena = "NOVENTA"
    else:
        decena = "NOVENTA Y "
#defino los numeros del 10 al 19
if resultado == 1:
    if resto == 0:
        nombre = "DIEZ"
    if resto == 1:
        nombre = "ONCE"
    if resto == 2:
        nombre = "DOCE"
    if resto == 3:
        nombre = "TRECE"
    if resto == 4:
        nombre = "CATORCE"
    if resto == 5:
        nombre = "QUINCE"
    if resto == 6:
        nombre = "DIECISEIS"
    if resto == 7:
        nombre = "DIECISIETE"
    if resto == 8:
        nombre = "DIECIOCHO"
    if resto == 9:
        nombre = "DIECINUEVE"
if (resultado == 0 and resto == 0) or resultado == 1:
    print("El numero ingresado es: ",nombre)
else:
    nombre = decena + unidad
    print("El numero ingresado es: ",nombre)