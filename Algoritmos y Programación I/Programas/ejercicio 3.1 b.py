def ingresoSegundos ():
    segundos=int(input("Ingrese una cantidad de segundos: "))
    return(segundos)
def calculoTiempo (segundos):
    horas = segundos//3600
    restohoras = segundos%3600
    minutos = restohoras//60
    restominutos= restohoras%60
    segundos= restominutos
    return(horas,minutos,segundos)
print("Ingrese una cantidad de segundos y el programa le devuelve el tiempo en horas, minutos y segundos.")
segundos=ingresoSegundos()
horas,minutos,segundos=calculoTiempo(segundos)
print("Hay un total de", horas ,"horas", minutos ,"minutos y", segundos ,"segundos")
