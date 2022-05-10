import random

def RataLoca(tiempo=0):
    camino=random.randrange(1,4)
    if camino==1:
        tiempo=tiempo+3
        print("Ole 1")
        RataLoca(tiempo)
        
    elif camino==2:
        tiempo=tiempo+5
        print("Ole 2")
        RataLoca(tiempo)
    else:
        tiempo=tiempo+7
        print("Salio de la jaula y tardo", tiempo ,"minutos")
            
RataLoca(0)