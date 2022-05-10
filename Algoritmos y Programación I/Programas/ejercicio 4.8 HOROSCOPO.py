mes=int(input("Ingrese el mes de su nacimiento en numero: "))
dia=int(input("Ingrese el dia de su nacimiento: "))
if mes > 12  or mes < 1 or dia > 31 or dia < 1:
    print("La fecha ingresada no es valida.")
if mes == 4 or mes == 6 or mes == 9 or mes == 11 :
        if dia > 30:
            print("La fecha no es valida")
else:
    if mes == 3 and dia > 20 or mes == 4 and dia < 21:
        signo = "ARIES"
    elif mes == 4 and dia > 20 or mes == 5 and dia < 21:
        signo = "TAURO"
    elif mes == 5 and dia > 20 or mes == 6 and dia < 22:
        signo = "GEMINIS"
    elif mes == 6 and dia > 21 or mes == 7 and dia < 24:
        signo = "CANCER"
    elif mes == 7 and dia > 23 or mes == 8 and dia < 24:
        signo = "LEO"
    elif mes == 8 and dia > 23 or mes == 9 and dia < 24:
        signo = "VIRGO"
    elif mes == 9 and dia > 23 or mes == 10 and dia < 23:
        signo = "LIBRA"
    elif mes == 10 and dia > 22 or mes == 11 and dia < 23:
        signo = "ESCORPIO"
    elif mes == 11 and dia > 22 or mes == 12 and dia < 22:
        signo = "SAGITARIO"
    elif mes == 12 and dia > 21 or mes == 1 and dia < 21:
        signo = "CAPRICORNIO"
    elif mes == 1 and dia > 20 or mes == 2 and dia < 20:
        signo = "ACUARIO"
    elif mes == 2 and dia > 19 or mes == 3 and dia < 21:
        signo = "ARIES"
print("Su signo en el horoscopo es:", signo)