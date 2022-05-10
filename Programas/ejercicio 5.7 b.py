def Ingreso ():
    num = int(input("Ingrese el numero hasta el que quiere buscar numeros perfectos: "))
    return(num)
def buscaPerfectos(num):
    for i in range(1,num+1):
        divisor=1
        suma=0
        while divisor<i:
            if i%divisor==0 and i!=1:
                suma=suma+divisor
            divisor+=1
        if i==suma:
            print(i,"es perfecto")
numero=Ingreso()
buscaPerfectos(numero)