def ingresoHoras():
    horas = int(input("Ingrese una cantidad de horas: "))    
    return(horas)
def ingresoMinutos():
    minutos=int(input("Ingrese una cantidad de minutos: "))
    return(minutos)
def ingresoSegundos():
    segundos=int(input("Ingrese una cantidad de minutos: "))
    return(segundos)
def calculoSegundos(horas,minutos,segundos):
    segundostotales = horas*3600 + minutos*60 +segundos
    return(segundostotales)
print("El programa le solicita un intervalo en horas, minutos y segundos, y devuelve la cantidad total de segundos.")
horas=ingresoHoras()
minutos=ingresoMinutos()
segundos=ingresoSegundos()
total=calculoSegundos(horas,minutos,segundos)
print("Hay un total de", total ,"segundos en", horas ,"horas,", minutos ,"minutos y", segundos ,"segundos.")