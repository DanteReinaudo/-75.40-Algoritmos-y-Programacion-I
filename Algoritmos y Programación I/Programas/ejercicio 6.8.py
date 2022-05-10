def Ingreso():
    codigo=input("Ingrese un numero en binario: ")
    return(codigo)
def base10(strn):
        l = len( strn ) - 1
        result = 0
        for i in strn:
                p = 2 ** l
                result = result + ( int(i) * p)
                l = l - 1
        return result
binario=Ingreso()
resultado=base10(binario)
print(resultado)