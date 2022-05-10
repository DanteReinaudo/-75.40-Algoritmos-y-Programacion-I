#Dante Reinaudo 102848 DEFINITIVO
def visitantesTotales(listaVisitantes):
    cantPuertaA=0
    cantPuertaB=0
    for i in range(0,len(listaVisitantes)):
        if listaVisitantes[i][0]=="A":
            cantPuertaA=cantPuertaA+1
        elif listaVisitantes[i][0]=="B":
            cantPuertaB=cantPuertaB+1
    print("Ingresaron", cantPuertaA ,"visitantes por la puerta A")
    print("Ingresaron", cantPuertaB ,"visitantes por la puerta B")
    
def porcentajeAbono(listaVisitantes):
    total=len(listaVisitantes)
    cantTarjeta=0
    cantEfectivo=0
    for i in range(0,len(listaVisitantes)):
        if listaVisitantes[i][5]=="tarjeta":
            cantTarjeta=cantTarjeta+1
        elif listaVisitantes[i][5]=="efectivo":
            cantEfectivo=cantEfectivo+1
    try:
        porcentajeTarjeta= (cantTarjeta/total)*100
        porcentajeEfectivo= (cantEfectivo/total)*100
        print("El",porcentajeEfectivo ,"% de las personas abono con efectivo")
        print("El",porcentajeTarjeta ,"% de las personas abono con tarjeta")
    except:#si no hay visitantes tendria error de division por 0
        print("No hay visitantes")
    
def promedioEdad(listaVisitantes):
    total=len(listaVisitantes)
    edades=0
    for i in range(0,len(listaVisitantes)):
        edades=edades+listaVisitantes[i][3]
    try:    
        promedio=edades/total
        print("El promedio de edad de los visitantes es", promedio)
    except:#si no hay visitantes tendria error de division por 0
        print("No hay visitantes")
        
def recaudaciones(listaVisitantes):
    nacionales=0
    juveniles=0
    jubilados=0
    extranjeros=0
    for i in range(0,len(listaVisitantes)):
        if listaVisitantes[i][4]=="nacional":
            nacionales=nacionales+25
        elif listaVisitantes[i][4]=="juvenil":
            juveniles=juveniles+10
        elif listaVisitantes[i][4]=="jubilado":
            jubilados=jubilados+8
        elif listaVisitantes[i][4]=="extranjero":
            extranjeros=extranjeros+30
    archivo=open("Recaudacion.txt","w")
    archivo.write("NACIONAL,"+str(nacionales)+"\n")
    archivo.write("JUBILADO,"+str(jubilados)+"\n")
    archivo.write("JUVENIL,"+str(juveniles)+"\n")
    archivo.write("EXTRANJERO,"+str(extranjeros)+"\n")
    archivo.close()
    
    
visitantes=[["A","Juan","italiano",20,"juvenil","tarjeta","10.30"],["A","Romano","italiano",77,"jubilado","tarjeta","10.30"],["B","Jorge","peruano",40,"extranjero","efectivo","4:20"],["A","Domingo","italiano",37,"nacional","tarjeta","11:00"]]
visitantesTotales(visitantes)
porcentajeAbono(visitantes)
promedioEdad(visitantes)
recaudaciones(visitantes)