def ingreso_numeros():
    numeros=input("Ingrese la secuencia de numeros separados por un espacio: ")
    cadena=numeros.split()
    print(cadena)
    return(cadena)
def empaka(cadena):   
    for i in range(0,len(cadena)):
        contador=1
        a=1
        if i!= len(cadena)-1 and i-1!=0:
            while cadena[i]==cadena[i+a] :
                contador=contador+1
                a=a+1
            if cadena[i]!=cadena[i-1]:
                tupla=(cadena[i],contador)
                print(tupla)
        a=1




chain=ingreso_numeros()
empaka(chain)