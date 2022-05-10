class Intervalo:
    def __init__(self,liminf,limsup):
        if liminf < limsup:
            self.liminf=liminf
            self.limsup=limsup
        else:
            self.liminf=limsup
            self.limsup=liminf
    def imprimir(self):
        print(self.liminf, self.limsup)
    def duracion(self):
        duraciondelintervalo= self.limsup - self.liminf
        print(duraciondelintervalo)
    def interseccion(self,intervalo2):
        if self.liminf >= intervalo2.liminf and self.liminf <= intervalo2.limsup:
            limiteInferior=self.liminf
        
        

intervalo1=Intervalo(5,10)
print(intervalo1.limsup)
intervalo2=Intervalo(10,12)
intervalo1.duracion()