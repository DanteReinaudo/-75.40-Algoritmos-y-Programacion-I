#Dante Reinaudo 102848 DEFINITIVO
import time
from random import randrange

def detectaErrores(mensaje,codigoError):
    idUser=input("Ingrese la id del usuario: ")
    fecha=time.strftime("%d/%m/%y")
    hora=time.strftime("%H:%M:%S")
    listaInfo=[idUser,str(codigoError),mensaje,fecha,hora]
    mensajeGuardado="|".join(listaInfo)
    print(mensajeGuardado)
    archivo=open("errores.log","a")
    archivo.write(mensajeGuardado+"\n")
    archivo.close()

def generaErrores(cantidadErrores):
    listaErrores=["Bad Request","Unauthorized","PaymentRequired","Forbidden","Not Found","Method not Allowed"]
    listaCodigo=[400,401,402,403,404,405]
    for i in range(0,cantidadErrores):
        errorRandom=randrange(0,len(listaErrores))
        codigoError=listaCodigo[errorRandom]
        mensajeError=listaErrores[errorRandom]
        detectaErrores(mensajeError,codigoError)
        
def cuentaErrores():
    archivo=open("errores.log","r")
    cant404=0
    cant505=0
    for linea in archivo:
        linea=linea.rstrip("\n")
        linea=linea.split("|")
        if linea[1]=="404":
            cant404=cant404+1
        elif linea[1]=="505":
            cant505=cant505+1
    archivo.close()
    print("En el log figuran", cant404,"errores del tipo 404")
    print("En el log figuran", cant505,"errores del tipo 505")

"""
def errorFrecuente():
    archivo=open("errores.log","r")
    lista= []
    dicc={}
    for linea in archivo:
        linea=linea.rstrip("\n")
        linea=linea.split("|")
        lista.append(linea[1])
    print(lista)
    ACA FALTARIA USAR UN DICCIONARIO PARA CONTAR LA CANTIDAD DE VECES QUE APARECE CADA ERROR 
    archivo.close()
"""
    
#detectaErrores("OK",200)
#detectaErrores("Unassigned",420)
#generaErrores(4)
#cuentaErrores()
errorFrecuente()