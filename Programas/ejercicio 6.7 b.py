def Ingreso ():
    cadena=[]
    palabra=str(input("Ingrese una cadena: "))
    cadena.append(palabra)
    opcion=str(input("Desea ingresar otra palabra (SI/NO)?: ")).upper()
    while opcion == "SI":
        palabra=str(input("Ingrese una cadena: "))
        cadena.append(palabra)
        opcion=str(input("Desea ingresar otra palabra (SI/NO)?: ")).upper()
    cadena.sort()
    print(cadena)
    print(cadena[0])
Ingreso()
