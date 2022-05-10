class Fraccion():
    def __init__(self,dividendo,divisor):
        self.dividendo=dividendo
        self.divisor=divisor
    def __str__(self):
        print(self.dividendo,"/",self.divisor)
    def __add__(self,fraccion):
        nuevodivisor = self.divisor * fraccion.divisor
        nuevodividendo = self.dividendo*fraccion.divisor + fraccion.dividendo*self.divisor
        return(Fraccion(nuevodividendo,nuevodivisor))
    def __mul__(self,fraccion):
        nuevodivisor= self.divisor * fraccion.divisor
        nuevodividendo= self.dividendo * fraccion.dividendo
        return(Fraccion(nuevodividendo,nuevodivisor))
    
    def simplificar(self):
        mcd=euclides(self.divisor,self.dividendo)
        divisorsimpl = self.divisor//mcd
        dividendosimpl= self.dividendo//mcd
        return(Fraccion(dividendosimpl,divisorsimpl))
        

def euclides(n,m):
    mcd = ""
    while mcd != n:
        resto = m%n
        if resto == 0:
            mcd = n
        else:
            m = n
            n = resto
    return(mcd)   
    
fraccion1=Fraccion(4,20)
fraccion2=Fraccion(3,40)
fraccionsimplif=fraccion1.simplificar()
fraccionsimplif.__str__()
sumafraccion=fraccion1.__add__(fraccion2)
sumafraccion.__str__()
productofraccion=fraccion1.__mul__(fraccion2)
productofraccion.__str__()