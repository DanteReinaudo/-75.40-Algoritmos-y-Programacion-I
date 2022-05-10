class Impresora():
    def __init__(self,nombre,tinta):
        self.nombre=nombre
        self.tinta=tinta
        self.cola=[]
    def encolar(self,nombre):
        self.cola.append(nombre)
    def imprimir(self):
        if len(self.cola)==0:
            print("No hay documentos para imprimir")
        elif self.tinta<1:
            print("No hay tinta suficiente")
        else:
            impreso=self.cola.pop(0)
            self.tinta=self.tinta-1
            print("El archivo", impreso ," ha sido impreso con exito")
    def cargar(self,cartucho):
        self.tinta=self.tinta + cartucho
        
class Oficina ():
    def __init__(self):
        self.impresoras=[]
    def agregar_impresoras(self,impresora):
        self.impresora.append(impresora)

impresora=Impresora("HP420",1)

impresora.imprimir()        
        
            