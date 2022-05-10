def Ingreso():
    digito=int(input("Ingrese un digito: "))
    while digito < 0 or digito > 9:
        print("Eso no es un digito")
        digito=int(input("Ingrese un digito: "))
    return(digito)
def Segundero(digito):
    if digito > 6:
        PRINT("no esta")
    else:
        print("si esta")