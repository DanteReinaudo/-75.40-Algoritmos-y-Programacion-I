num = int(input("Ingrese un numero entero: "))
resto = num % 2
if resto == 0:
    print("El numero", num ,"es par")
elif resto == 1:
    print("El numero", num ,"es impar")
a=0
for i in range(1,num+1):
    if(num % i==0):
        a=a+1
if(a!=2):
    print("El numero", num ,"no es primo")
else:
    print("El numero", num ," es primo")
