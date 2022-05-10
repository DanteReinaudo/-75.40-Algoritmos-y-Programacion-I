print("Este programa le pide un dia del año y le dice que dia de la semana es teniendo en cuenta que el primer dia del año es lunes.")
dia = int(input("Ingrese un dia del año: "))
while dia < 1 or dia > 366:
    print("Dia no valido")
    dia = int(input("Ingrese un dia del año: "))
if dia % 7 == 0:
    print("El dia", dia ,"es domingo")
elif dia % 6 == 0:
    print("El dia", dia ,"es sabado")
elif dia % 5 == 0:
    print("El dia", dia ,"es viernes")
elif dia % 4 == 0:
    print("El dia", dia ,"es jueves")
elif dia % 3 == 0 and dia % 6 != 0:
    print("El dia", dia ,"es miercoles")
elif dia % 2 == 0 and dia % 6 != 0 and dia % 4 != 0:
    print("El dia", dia ,"es martes")
else:
    print("El dia", dia ,"es lunes")
    