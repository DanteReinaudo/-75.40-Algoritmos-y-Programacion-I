def digito(numero,digitos):
    while digitos*10 <= numero:
        digitos=digitos*10
        digito(numero,digitos)
    
    if digitos >= numero:
        cantidad=str(digitos)
        print("El numero tiene", len(cantidad),"digitos")
        

digito(1000,1)