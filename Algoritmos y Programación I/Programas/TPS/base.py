from random import randint
import time

def Genera_Matriz(logotablero):
    matriz=[]
    for i in range (6): #filas
        matriz.append([])
        for j in range (6):
            matriz[i].append(logotablero) #columnas
    contador=1
    for i in range (1,6): 
        matriz[0][0]="©©"
        if i<10:
            matriz[i][0]="0"+str(contador)
            matriz[0][i]="0"+str(contador)
        else:
            matriz[i][0]=str(contador)
            matriz[0][i]=str(contador)
        contador=contador+1
    return(matriz)

def Muestra_Matriz(matriz):
    for i in range (6):
            print(matriz[i])        

def Bombas_Random(matriz,cantbombas,logotablero,logobomba):
    while cantbombas > 0:
        a=randint(1,5)
        b=randint(1,5)
        if matriz[a][b]==logotablero:
            matriz[a][b]=logobomba
            cantbombas=cantbombas-1
    return(matriz)

def Busca_Bombas(MatrizImagen,MatrizRandom,cantbombas,k,logotablero,logobomba,nivel):
    vidas=4
    liberadas=0
    while vidas>0 and liberadas!=(25-cantbombas):
        print("Busca Bombas".center(125,"~"))
        Muestra_Matriz(MatrizImagen)
        print()
        print("Ingrese la coordenada, de no ingresar un entero el programa pinchará, tome conciencia de sus acciones: ")
        fila=int(input("Ingrese un numero de fila: "))
        while fila > 5 or fila < 1:
            print("Esa fila no existe.")
            fila=int(input("Ingrese un numero de fila: "))
        columna=int(input("Ingrese un numero de columna: "))
        while columna > 5 or columna < 1 :
            print("Esa fila no existe.")
            columna=int(input("Ingrese un numero de fila: "))
        
        if MatrizRandom[fila][columna]==logobomba:
            MatrizImagen[fila][columna]=logobomba
            vidas=vidas-1
            print("Oh no! Has tocado una bomba. Pierdes una vida.".center(125," "))
            print()
            time.sleep(2)
        elif MatrizImagen[fila][columna]==logotablero:
            contador=0
            if fila==1 and columna==1:
                for i in range(1,3):
                    for j in range (1,3):
                        if MatrizRandom[i][j]!=logobomba:
                            if i==fila and j == columna:
                                contador=contador
                            else:
                                contador=contador+1
            elif fila==1 and columna==5:
                for i in range(1,3):
                    for j in range (4,6):
                        if MatrizRandom[i][j]!=logobomba:
                            if i==fila and j == columna:
                                contador=contador
                            else:
                                contador=contador+1
            elif fila==5 and columna==1:
                for i in range(4,6):
                    for j in range (1,3):
                        if MatrizRandom[i][j]!=logobomba:
                            if i==fila and j == columna:
                                contador=contador
                            else:
                                contador=contador+1
            elif fila==5 and columna==5:
                for i in range(4,6):
                    for j in range (4,6):
                        if MatrizRandom[i][j]!=logobomba:
                            if i==fila and j == columna:
                                contador=contador
                            else:
                                contador=contador+1
            elif fila==1 and columna!=1 and columna!=5:
                for i in range(1,3):
                    for j in range (columna-1,columna+2):
                        if MatrizRandom[i][j]!=logobomba:
                            if i==fila and j == columna:
                                contador=contador
                            else:
                                contador=contador+1
            elif fila==5 and columna!=1 and columna!=5:
                for i in range(4,6):
                    for j in range (columna-1,columna+2):
                        if MatrizRandom[i][j]!=logobomba:
                            if i==fila and j == columna:
                                contador=contador
                            else:
                                contador=contador+1
            elif columna==1 and fila!=1 and fila!=5:
                for i in range(fila-1,fila+2):
                    for j in range (1,3):
                        if MatrizRandom[i][j]!=logobomba:
                            if i==fila and j == columna:
                                contador=contador
                            else:
                                contador=contador+1
            elif columna==5 and fila!=1 and fila!=5:
                for i in range(fila-1,fila+2):
                    for j in range (4,6):
                        if MatrizRandom[i][j]!=logobomba:
                            if i==fila and j == columna:
                                contador=contador
                            else:
                                contador=contador+1
            else:
                for i in range(fila-1,fila+2):
                    for j in range (columna-1,columna+2):
                        if MatrizRandom[i][j]!=logobomba:
                            if i==fila and j == columna:
                                contador=contador
                            else:
                                contador=contador+1
                
            contador="~"+str(contador)
            MatrizImagen[fila][columna]=contador
            liberadas=liberadas+1
    if vidas==0:
        print("Que pena, ha perdido, más suerte la proxima vez")
        nombre=input("Ingrese su nombre: ")
        tuplascore=("Partida Perdida",nivel,nombre)
    else:
        Muestra_Matriz(MatrizImagen)
        print("Felicitaciones, ha ganado!".center(125,"+"))
        puntaje=(liberadas*k)-(5*(4-vidas))
        nombre=input("Ingrese su nombre: ")
        tuplascore=(puntaje,nivel,nombre)
        
    return(tuplascore)

def Menu():
    opcion=""
    LogoTablero="╠╣"
    logobombas="><"
    historial=[]
    Top3=[]
    puntaje=()
    while opcion!="E":
        titulo="╣Busca Bombas╠"
        print (titulo.center(125,"═"))
        print()
        print("Bienvenid@ usuario a nuestro juego, ingrese la letra de la opcion que desea ejecutar".center(125,"~"))
        print()
        print("(A)JUGAR")
        print("(B)PUNTAJES")
        print("(C)INSTRUCCIONES")
        print("(D)CONFIGURACIONES")
        print("(E)SALIR")
        opcion=input("                                                         (A/B/C/D/E):").upper()
        
        while opcion != "A" and opcion != "B" and opcion != "C" and opcion != "D" and opcion != "E":
            print("Lo siento, el valor ingresado no es valido.")
            opcion=input("                                                         (A/B/C/D/E):").upper()
        print()
        if opcion == "A":
            dificultad=input("Elija una dificultad [(1)Fácil (2)Medio (3)Dificil]:")
            while dificultad!="1" and dificultad!="2" and dificultad!="3":
                print("La dificultad ingresada no es vallida")
                dificultad=input("Elija una dificultad [(1)Fácil (2)Medio (3)Difícil]:")
                print()
            if dificultad=="1":
                bombas=2
                K=1
                nivel="Fácil"
            elif dificultad=="2":
                bombas=20
                K=2
                nivel="Medio"
            elif dificultad=="3":
                bombas=35
                K=3
                nivel="Difícil"
            matrizImagen=Genera_Matriz(LogoTablero)
            matrizTablero=Genera_Matriz(LogoTablero)
            matrizRandom=Bombas_Random(matrizTablero,bombas,LogoTablero,logobombas)
            Muestra_Matriz(matrizRandom)
            puntaje=Busca_Bombas(matrizImagen,matrizRandom,bombas,K,LogoTablero,logobombas,nivel)
            historial.append(puntaje)
            if puntaje[0]!="Partida Perdida":
                Top3.append(puntaje)
        elif opcion == "B":
            print("PUNTAJES".center(125," "))
            print()
            opcionscore=input("Elija una opcion [A)Top 3 B)Historial ultimas 10 partidas]: ").upper()
            while opcionscore!="A" and opcionscore!="B":
                print("Opcion no valida, ingrese otra nuevamente")
                opcionscore=input("Elija una opcion [A)Top 3 B)Historial ultimas 10 partidas]: ").upper()
            if opcionscore=="A":
                print("TOP 3".center(125,"~"))
                if len(Top3)==0:
                    print("Aun no se ha ganado ninguna partida".center(125," "))
                else:
                    Top3.sort()
                    while len(Top3)>3:
                        Top3.pop(0)
                    Top3.reverse()
                    #Siempre que use un for me tiro un error 
                    if len(Top3)==1:
                        print(Top3)
                    elif len(Top3)==2:
                        print(Top3[0])
                        print(Top3[1])
                    elif len(Top3)==3:
                        print(Top3[0])
                        print(Top3[1])
                        print(Top3[2])
                
            if opcionscore=="B":
                print("Historial de ultimas 10 partidas".center(125,"~"))
                while len(historial)>10:
                    historial.pop(0)
                if len(historial)==0:
                    print("Todavia no se ha jugado ninguna partida.".center(125," "))
                else:
                    for i in range (0,len(historial)):
                        print(historial[i])
            print()
        elif opcion == "C":
            print()
            print("INSTRUCCIONES".center(125," "))
            print("El objetivo del Busca-Bombas es liberar la mayor cantidad de casillas sin que se agoten las vidas. En cada partida el jugador contará con 4 vidas y perderá una cada vez que ingrese un casillero donde hay una bomba, en caso de acabarse las vidas el jugador pierde automáticamente.")
            print("El usuario debe elejir una dificultad antes de ingresar, a mayor dificultad, mayor cantidad de bombas en el tablero, FÁCIL = 10 BOMBAS, MEDIO = 20 BOMBAS , DIFICIL = 35 BOMBAS.")
            print("Una vez iniciado el juego, al usuario se le pedira que ingrese una coordenada del tablero, si en esta hay una bomba perdera una vida, en caso de que no haya se liberará dicha casilla y mostrará cuantas casillas contiguas a ésta no contienen bombas.")
            print()
        elif opcion == "D":
            print("CONFIGURACIONES".center(125," "))
            print("Elija el logo que mas prefiera:")
            opcionbomba=input("Elija el logo de la bomba [A)>< B)▒▒ C)¶ß]: ").upper()
            while opcionbomba != "A" and opcionbomba != "B" and opcionbomba != "C":
                print("Opcion no valida")
                opcionbomba=input("Elija el logo de la bomba [A)>< B)▒▒ C)¶ß]: ").upper()
            if opcionbomba=="A":
                logobombas="><"
            elif opcionbomba=="B":
                logobombas="▒▒"
            elif opcionbomba=="C":
                logobombas="¶ß"
            opcionlogo=input("Elija el estilo del tablero [A)╠╣ B)╬╬ C)╚╗ D)██]: ").upper()
            while opcionlogo != "A" and opcionlogo != "B" and opcionlogo != "C" and opcionlogo != "D":
                opcionlogo=input("Elija el estilo del tablero [A)╠╣ B)╬╬ C)╚╗ D)██]: ").upper()
            if opcionlogo=="A":
                LogoTablero="╠╣"
            elif opcionlogo=="B":
                LogoTablero="╬╬"
            if opcionlogo=="C":
                LogoTablero="╚╗"
            if opcionlogo=="D":
                LogoTablero="██"
            print()
        time.sleep(3)
            
    if opcion == "E":
        print()
        print("Gracias por utilizar nuestro programa".center(125,"~"))
        print("©".center(125,"~"))
        exit()
                
Menu()