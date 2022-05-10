def ingresoNumeros(orden):
    num=int(input("Ingrese el {0} numero: ".format(orden)))
    return(num)
def euclides(n,m):
    mcd = ""
    while mcd != n:
        resto = m%n
        if resto == 0:
            mcd = n
        else:
            m = n
            n = resto
    return(mcd)
print("Este programa le pide dos numeros y devuelve el maximo comun divisior entre ellos")
num1 = ingresoNumeros("primer")
while num1 == 0:
    print("No puedo dividir por 0 Capo!")
    num1 = ingresoNumeros("primer")
num2 = ingresoNumeros("segundo")
while num2 == 0:
    print("No puedo dividir por 0 Capo!")
    num2 = ingresoNumeros("segundo")
MaximoCD= euclides(num2,num1)
print("El maximo comun divisor entre", num1 ,"y", num2 ,"es", MaximoCD)