print("Ingrese un año y este programa lo convierte en numeros romanos.")
año = int(input("Ingrese un año: "))

mil = año // 1000
restomil = año%1000

novecientos = restomil//900
restonovecientos= restomil%900

quinientos = restonovecientos//500
restoquinientos=restonovecientos%500

cuatrocientos=restoquinientos//400
restocuatrocientos=restoquinientos%400

cien=restocuatrocientos//100
restocien=restocuatrocientos%100

noventa=restocien//90
restonoventa=restocien%90

cincuenta=restonoventa//50
restocincuenta=restonoventa%50

cuarenta=restocincuenta//40
restocuarenta=restocincuenta%40

diez=restocuarenta//10
restodiez=restocuarenta%10

nueve=restodiez//9
restonueve=restodiez%9

cinco=restonueve//5
restocinco=restonueve%5

cuatro=restocinco//4
restocuatro=restocinco%4

uno=restocuatro//1
romano=(mil*'M'+novecientos*'CM'+quinientos*'D'+cuatrocientos*'CD'+cien*'C'+noventa*'XC'+cincuenta*'L'+cuarenta*'XL'+diez*'X'+nueve*'IX'+cinco*'V'+cuatro*'IV'+uno*'I')
#3 EPÍLOGO
#3.1 Exhibición de resultados
if 1<=año <4000: print('El número', año, 'en el sistema romano se escribe', romano)
elif año==0: print('ERROR: El número cero NO EXISTE en el sistema romano.')
elif año >=4000: print('ERROR: No se pueden convertir números mayores a 3999.')