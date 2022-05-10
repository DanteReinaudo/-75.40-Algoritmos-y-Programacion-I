class Caja():
    def __init__(self,diccionario):
        parametros=[1000,500,200,100,50,20,10,5,2,1]
        keys=list(diccionario.keys())
        values=list(diccionario.values())
        dicc={1000:0 ,500: 0 , 200:0 ,100:0 ,50:0 ,20:0 ,10:0 ,5:0 ,2:0 ,1:0 }
        for i in range (0,len(keys)):
            if keys[i] not in parametros:
                print("Error", keys[i] ,"no es una denominacion valida.")
            else:
                dicc[keys[i]]=values[i]
        self.dicc=dicc
        valores=list(self.dicc.values())
        claves=list(self.dicc.keys())
        self.valores=valores
        self.claves=claves
    def refresh(self):
        valores=list(self.dicc.values())
        claves=list(self.dicc.keys())
        self.valores=valores
        self.claves=claves
    def __str__(self):
        self.refresh()
        cantidad=0
        for i in range (0,len(self.valores)):
            cantidad=cantidad+self.valores[i]*self.claves[i]
        print("Caja: ",self.dicc,"total:", cantidad ,"pesos")
    def agregar(self,caja):
        self.refresh()
        for i in range(0,len(caja.claves)):
            self.dicc[caja.claves[i]]=self.dicc[self.claves[i]]+caja.dicc[self.claves[i]]
    def quitar(self,caja):
        self.refresh()
        for i in range(0,len(caja.claves)):
            self.dicc[caja.claves[i]]=self.dicc[self.claves[i]]-caja.dicc[self.claves[i]]
diccionario={500:2 ,200: 7, 100: 0}
diccionario2={1000: 20 , 100:2 ,1 :420}
caja1=Caja(diccionario)
caja2=Caja(diccionario2)
diccionario3={1000: 10 , 100:2 ,1 :420, 5: 20}
caja3=Caja(diccionario3)
caja1.agregar(caja2)
caja1.__str__()
caja1.quitar(caja3)
caja1.__str__()