from pyowm import OWM
import time
import random
OWMKEY="ab80e05035de9a636ccca6c4250dfa6d"

def keyOwm(key):
    "pide la key de la api y devuelve el objeto owm"
    objeto = OWM(key)
    return(objeto)

def obtenerClima(objeto):
    "La funcion recibe el objeto obtenido con keyOwm, devuelve tupla hora/fecha, el porcentaje de nubes y la temperatura en C"
#    lugar=objeto.weather_at_coords(-34.61, -58.38)
    lugar=objeto.weather_at_place("Buenos Aires, AR")
    clima=lugar.get_weather()
    temperaturas=clima.get_temperature(unit='celsius')
    temperaturaActual=temperaturas["temp"]
    nubes=clima.get_clouds()
    lluvias=clima.get_rain() #si no llueve devuelve diccionario vacio
    fecha=time.strftime("%d/%m/%y")
    hora=time.strftime("%H:%M:%S")
    tiempo=(hora,fecha)
    return(temperaturaActual,nubes,tiempo)
    
owm=keyOwm(OWMKEY)
temp,nubes,tiempo=obtenerClima(owm)
print(temp)
print(nubes)
print(tiempo)
print(random.randrange(100))