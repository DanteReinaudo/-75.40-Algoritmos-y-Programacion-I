def IngresoTexto():
    texto=input("Ingrese un texto: ")
    texto=texto.split()
    return(texto)
def CuentaPalabra(texto):
    frecuencia=[]
    for palabra in texto:
        print(palabra)
        frecuencialetra=[]
        for caracter in palabra:
            
            print(caracter)
            frecuencialetra.append(palabra.count(caracter))
        frecuencia.append(frecuencialetra)
    print(frecuencia)
texto=IngresoTexto()
CuentaPalabra(texto)