def Ingreso(orden):
    num = int(input("Ingrese el {0} numero entero positivo: ".format(orden)))
    return(num)
def buscaMultiplos(num1,num2):
    contador=0
    multiplo=1
    while multiplo*num1<num2:
        contador+=1
        print(multiplo*num1 ,"es multiplo de", num1 ,"y es menor a", num2)
        multiplo+=1
    return(contador)
print("Ingrese dos numeros enteros, y el programa le dice cuantos multiplos del primero hay que son menores al segundo")
num1=Ingreso("primer")
num2=Ingreso("segundo")
total=buscaMultiplos(num1,num2)
print("Hay un total de", total ,"numeros multiplos de", num1 ,"que son menores a", num2)