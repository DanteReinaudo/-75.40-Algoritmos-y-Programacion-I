num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

for i in range (num1,num2+1):
    if i%2 == 0:
        print(i)
for i in range (num2,num1+1):
    if i%2 == 0:
        print(i)
        