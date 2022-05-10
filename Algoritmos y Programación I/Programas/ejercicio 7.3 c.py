def Ingreso_Nombre():
    lista=[]
    opcion="SI"
    while opcion!="NO":
        nombre=input("Ingrese su nombre: ")
        genero=input("Ingrese su genero Masculino/Femenino: ").upper()
        while genero!="MASCULINO" and genero!="FEMENINO":
            genero=input("Ingrese su genero Masculino/Femenino: ").upper()
        tupla=(nombre,genero)
        lista.append(tupla)
        opcion=input("Desea ingresar otro nombre? (SI/NO): ").upper()
    return(lista)
def voto(lista):
    for i in range(0,len(lista)):
        if lista[i][1]=="MASCULINO":
            print("Querido", lista[i][0],"vote por mi")
        elif lista[i][1]=="FEMENINO":
            print("Querida", lista[i][0],"vote por mi")
lista=Ingreso_Nombre()
voto(lista)
        
