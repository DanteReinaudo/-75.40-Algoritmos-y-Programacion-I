def fInclusiva(fileviejo,fileinclusivo):
    archivoViejo=open(fileviejo,"r")
    listaPalabras=[]
    for linea in archivoViejo:
        linea=linea.rstrip("\n")
        linea=linea.split()
        oracionesInclusivas=[]
        for palabra in linea:
            if palabra.endswith("o")==True or palabra.endswith("a")==True:
                palabra=palabra[0:len(palabra)-1]
                palabraInclusiva=palabra+"e"
            elif palabra.endswith("os")==True or palabra.endswith("as")==True:
                palabra=palabra[0:len(palabra)-2]
                palabraInclusiva=palabra+"es"
            else:
                palabraInclusiva=palabra
            oracionesInclusivas.append(palabraInclusiva)
        listaPalabras.append(oracionesInclusivas)
    archivoViejo.close()
    archivoInclusivo=open(fileinclusivo,"w")

    for oracion in listaPalabras:
        inclusive=" ".join(oracion)
        inclusive=inclusive+"\n"
        archivoInclusivo.write(inclusive)
           
    archivoInclusivo.close()


fInclusiva("texto no inclusivo.txt","texto inclusive.txt")
