def ingresoTiempo(numero):
    horas = int(input("Ingrese la cantidad de horas del intervalo {0} : ".format(numero)))
    minutos=int(input("Ingrese la cantidad de minutos del intervalo {0} : ".format(numero)))
    segundos=int(input("Ingrese la cantidad de segundos del intervalo {0} : ".format(numero)))
    return(horas,minutos,segundos)
def calculoSegundos(horas,minutos,segundos):
    segundostotales = horas*3600 + minutos*60 +segundos
    return(segundostotales)
def sumaTiempo (tiempo1,tiempo2):
    total=tiempo1+tiempo2
    return(total)
def calculoTiempo (segundos):
    horas = segundos//3600
    restohoras = segundos%3600
    minutos = restohoras//60
    restominutos= restohoras%60
    segundos= restominutos
    return(horas,minutos,segundos)

print("El programa le solicita dos intervalos en horas, minutos y segundos, y devuelve la cantidad total en horas, minutos y segundos.")
hora1,minuto1,segundo1=ingresoTiempo(1)
hora2,minuto2,segundo2=ingresoTiempo(2)
segundostotales1=calculoSegundos(hora1,minuto1,segundo1)
segundostotales2=calculoSegundos(hora2,minuto2,segundo2)
totalsegundos=sumaTiempo(segundostotales1,segundostotales2)
horatotal,minutototal,segundototal=calculoTiempo(totalsegundos)
print("Hay un total de", horatotal ,"horas", minutototal ,"minutos y", segundototal ,"segundos")