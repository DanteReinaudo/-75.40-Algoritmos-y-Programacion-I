class TorreDeControl():
    def __init__(self):
        self.arribos=[]
        self.despegues=[]
    def nuevo_arribo(self,nombre):
        self.arribos.append(nombre)
    def nueva_partida(self,nombre):
        self.despegues.append(nombre)
    def ver_estado(self):
        print("Vuelos esperando aterrizar: ", self.arribos)
        print("Vuelos esperando despegar: ", self.despegues)
    def asignar_pista(self):
        if len(self.arribos)!=0:
            arribo=self.arribos.pop(0)
            print("El vuelo", arribo ,"ha aterrizado con exito")
        elif len(self.arribos)==0 and len(self.despegues)!=0:
            despego=self.despegues.pop(0)
            print("El vuelo", despego ,"ha despegado con exito")
        else:
            print("No hay vuelos en espera")
torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
