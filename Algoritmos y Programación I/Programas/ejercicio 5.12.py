def Ingreso_Examen():
    print("Bievenido a nuestro programa")
    cantejercicios=int(input("Ingrese la cantidad de ejercicios del examen: "))
    paraaprobar=float(input("Ingrese el porcentaje de ejercicios bien resueltos, nesecarios para aprobar el examen: "))
    return(cantejercicios,paraaprobar)

def apruebo(cantejercicios,paraaprobar):
    aprobado= (cantejercicios*paraaprobar)/100
    return(aprobado)

def Ingreso_Alumnos(cantejercicios,aprobado):
    alumno=input("Ingrese el nombre del alumno 1: ")
    nro=1
    ejresueltos=float(input("Ingrese la cantidad de ejercicios resueltos: "))
    while ejresueltos > cantejercicios:
        print("Ingreso mas ejercicios de los que hay en el parcial.")
        ejresueltos=float(input("Ingrese la cantidad de ejercicios resueltos: "))
    print("El alumno ha resuelto el", (ejresueltos/cantejercicios)*100 ,"por ciento del examen")
    if ejresueltos >= aprobado:
        print("Felicitaciones el alumno", alumno ,"ha aprobado")
    else:
        print("El alumno", alumno ,"no ha aprobado")
    opcion=input("Desea ingresar mas examenes (SI/NO)?: ").upper()
    while opcion == "SI":
        nro +=1
        alumno=input("Ingrese el nombre del alumno {0}: ".format(nro))
        ejresueltos=float(input("Ingrese la cantidad de ejercicios resueltos: "))
        while ejresueltos > cantejercicios:
            print("Ingreso mas ejercicios de los que hay en el parcial.")   
        print("El alumno ha resuelto el", (ejresueltos/cantejercicios)*100 ,"por ciento del examen")
        if ejresueltos >= aprobado:
            print("Felicitaciones el alumno", alumno ,"ha aprobado")
        else:
            print("El alumno", alumno ,"no ha aprobado")
        opcion=input("Desea ingresar mas examenes (SI/NO)?: ").upper()
cantidad,aprobar=Ingreso_Examen()
aprobado=apruebo(cantidad,aprobar)
Ingreso_Alumnos(cantidad,aprobado)
    