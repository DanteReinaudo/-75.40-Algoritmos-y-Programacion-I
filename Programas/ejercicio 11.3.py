class Vector():
    def __init__(self,lista):
        self.lista=lista
    def __str__(self):
        print(self.lista)
    def __add__(self,vector):
        nuevalista=[]
        if len(self.lista) == len(vector.lista):
            for i in range(0,len(self.lista)):
                nuevacoordenada=self.lista[i] + vector.lista[i]
                nuevalista.append(nuevacoordenada)
        else:
            print("Los vectores no pueden ser sumados")
        return(Vector(nuevalista))
    def __mul__(self,num):
        nuevalista=[]
        for i in range(0,len(self.lista)):
            nuevacoordenada=self.lista[i]*num
            nuevalista.append(nuevacoordenada)
        return(Vector(nuevalista))
            
vector1=Vector([1,2,3])
vector1.__str__()
vector2=Vector([4,5,6])
vectorsuma=vector1.__add__(vector2)
vectorsuma.__str__()
vectormult=vector1.__mul__(10)
vectormult.__str__()
