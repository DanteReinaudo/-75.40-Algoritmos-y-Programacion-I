import datetime
print("Ingrese una fecha en formato (dia/mes/año)")
año = int(input("Ingrese un año: "))
mes = int(input("Ingrese un mes: "))
dia = int(input("Ingrese un dia: "))
fecha=datetime.datetime(año,mes,dia)
findeaño=datetime.datetime(año,12,31)
faltan=findeaño - fecha
print("Faltan", faltan ,"dias para fin de año.")