import json
import time
import spotipy
import spotipy.util as util
from pyowm import OWM
from random import randrange
from collections import OrderedDict
import csv

SCOPE = 'playlist-modify-public'
CLIENTID = '12a006cfd712418e86d2c660c6bb0b2e'
SECRETID = '5f1db05c4d26454f8c4fd09209d4c150'
RED_URI = 'https://www.google.com.ar/'
USER = 'ii4hjin5jvi883c76z6855plz'
OWMKEY="ab80e05035de9a636ccca6c4250dfa6d"

def autorizacion():
    "Genera el TOKEN de Spotipy"
    bandera=True
    while bandera:
        try:
            token = util.prompt_for_user_token(USER,SCOPE,CLIENTID,SECRETID,RED_URI)
            objeto = spotipy.Spotify(auth=token)
            bandera=False
        except:
            print("Error, no se puede obtener informacion del usuario.")
    return objeto

def keyOwm(key):
    "Pide la key de la api y devuelve el objeto owm"
    objeto = OWM(key)
    return(objeto)

def obtenerClima(key):
    "La funcion recibe la keyOwm, devuelve tupla hora/fecha, el porcentaje de nubes y la temperatura en C"
    owm=keyOwm(key)
    #lugar=objeto.weather_at_coords(-34.61, -58.38)
    lugar=owm.weather_at_place("Buenos Aires, AR")
    clima=lugar.get_weather()
    temperaturas=clima.get_temperature(unit='celsius')#devuelve diccionario con varias temp, max, min etc
    temperaturaActual=temperaturas["temp"]
    nubes=clima.get_clouds()
    lluvias=clima.get_rain() #si no llueve devuelve diccionario vacio
    fecha=time.strftime("%d/%m/%y")
    hora=time.strftime("%H:%M:%S")
    tiempo=(hora,fecha)
    return(temperaturaActual,nubes,tiempo,lluvias)

def validarEnteros(mensaje):
    "Valida el ingreso de enteros, recibe el mensaje del input, devuelve el numero entero validado"
    bandera=True
    while bandera:
        try:
            entero=int(input(mensaje))
            bandera=False
        except ValueError:
            print("La opcion ingresada no es valida")
    return(entero)

def tracksId(user,objeto,playlistId):
    """Ingresa el URI del USER, el objeto de SPOTIPY y la ID  de una playlist
    Saca el id de los tracks de una playlist, los devuelve en lista"""
    playlistTracks=objeto.user_playlist_tracks(user, playlistId,limit=100, market="AR")
    listaId=[]
    if len(playlistTracks["items"]) != 0:
        for tracks in range(0,len(playlistTracks["items"])):
            trackId=playlistTracks["items"][tracks]["track"]["id"]
            listaId.append(trackId)
    return(listaId)

def generarListaDeTracks(user,objeto,listaPlaylist):
    "Recibe una lista con el id de varias playlist y genera una lista mas grande con todos los tracks"
    listaDeTracks=[]
    for i in range(0,len(listaPlaylist)):
        tracks=tracksId(user,objeto,listaPlaylist[i])
        for j in range(0,len(tracks)):
            listaDeTracks.append(tracks[j])
    return(listaDeTracks)

def generarListaRandom(user,objeto,plid):
    "la use para la playlist del clima, pide la id de la playlist y devuelve lista de canciones random de dicha playlist sin repetir"
    dicc={}
    tracks=generarListaDeTracks(user,objeto,plid)
    for i in range(0,25):
        randomTrack=randrange(len(tracks))
        dicc[tracks[randomTrack]]=tracks[randomTrack]
    listaTracks=list(dicc.values())
    return(listaTracks)

def generarPlaylistSegunClima(user,objeto,KeyOWM):
    """recibe la key de la api pyOWM, borra todas las canciones que hay en la playlist, muestra el clima actual y la hora, dependiendo del clima
       genera una playlist, si el clima es diferente a los especificados para playlist imprime un mensaje. No devuelve nada"""
    temperatura,nubes,tiempo,lluvias=obtenerClima(KeyOWM)
    print("Hoy es", tiempo[1] ,"son las", tiempo[0],"la temperatura es de", temperatura,"° y hay un", nubes,"% de nubes en el cielo.")
    plidClima=objeto.user_playlists(user)['items'][-1]['id']
    climaTracksId=tracksId(user,objeto,plidClima)  
    if len(climaTracksId)!=0: #cada vez q se ejecuta borra todas las canciones anteriores anterior
        playlistRemovida=objeto.user_playlist_remove_all_occurrences_of_tracks(user, plidClima, climaTracksId)
    
    if nubes>80 and temperatura<=18 or nubes>60 and len(lluvias)!=0:
        sadPlaylistID=["37i9dQZF1DWX83CujKHHOn","37i9dQZF1DX2pSTOxoPbx9","37i9dQZF1DX4jSp9PHDkEC","37i9dQZF1DWT0qByOJYmmJ"]
        sadTracks=generarListaRandom(user,objeto,sadPlaylistID)
        objeto.user_playlist_add_tracks(user,plidClima,sadTracks)
        print("La playlist ha sido actualizada para este momento melancolico.")    
    elif nubes<60 and temperatura>19 and len(lluvias)==0:
        activoPlaylistID=["37i9dQZF1DX0hWmn8d5pRe","37i9dQZF1DXadOVCgGhS7j","37i9dQZF1DX9ZKyQHcEFXZ"]
        activoTracks=generarListaRandom(user,objeto,activoPlaylistID)
        objeto.user_playlist_add_tracks(user,plidClima,activoTracks)
        print("La playlist ha sido actualizada para que ejercite duro, que lo disfrute.")    
    elif len(lluvias)==0 and int(tiempo[0][0])==0 and int(tiempo[0][1]) <= 7:
        joditaPlaylistID=["37i9dQZF1DWUlCmB8llCTB","37i9dQZF1DWZjqjZMudx9T","37i9dQZF1DWTkIwO2HDifB","37i9dQZF1DXdMS2nFQ7EO0"]
        joditaTracks=generarListaRandom(user,objeto,joditaPlaylistID)
        objeto.user_playlist_add_tracks(user,plidClima,joditaTracks)
        print("La playlist ha sido actualizada para la jodita, que lo disfrute.")
    else:
        print("El clima no coincide con los parametros dados")
    input("Presione Enter para volver al Menú...")
    
def topArtistasPais(user,objeto,plid):
    """Ingresa el URI del USER, el objeto de SPOTIPY y
    el ID de la playlist de top 50 del país, imprime una lista con los top 10 artistas"""
    listaTracks=tracksId(user,objeto,plid)
    diccTopArtistas={}
    puesto=0
    for track in range(0,len(listaTracks)):
        jsonTrack=objeto.track(listaTracks[track])
        for i in range(0,len(jsonTrack["album"]["artists"])):
            artistaId=jsonTrack["album"]["artists"][i]["id"]
            jsonArtist=objeto.artist(artistaId)
            popularidad=jsonArtist["popularity"]
            if popularidad>90:
                diccTopArtistas[artistaId]=jsonArtist["name"]
    for key in diccTopArtistas:
        puesto=puesto+1
        print (puesto,")", diccTopArtistas[key])
     
def verPlaylistsTracks(user,objeto,playlistId):
    """Ingresa la URI del USER, el objeto de SPOTIPY y
    el ID de la playlist que se desee e imprime los tracks que contenga"""
    playlistTracks=objeto.user_playlist_tracks(user, playlistId,limit=100, market="AR")
    if len(playlistTracks["items"])== 0:
        print("La playlist no tiene ningun track.")
    else:
        print("Estos son los tracks de la playlist: ")
        for tracks in range(0,len(playlistTracks["items"])):
            infoTrack=(playlistTracks["items"][tracks]["track"]["name"],playlistTracks["items"][tracks]["track"]["artists"][0]["name"])
            print(tracks+1,"-",infoTrack)
            
def verPlaylists(user,objeto):
    """Ingresa la URI del USER y el objeto de SPOTIPY
    imprime las playlists ya creadas"""
    cantPlaylist = len(objeto.user_playlists(USER)['items'])
    if cantPlaylist != 0:
        for i in range(cantPlaylist):
            print(str(i+1) + '- ' + str(objeto.user_playlists(user)['items'][i]['name']))
    else:
        print('No hay playlists creadas.')
        
def playlistsCreadas(user,objeto):
    """Ingresa la URI del USER y el objeto de SPOTIPY
    Muestra las playlist, permite elegir una e imprime los tracks de esa playlist"""
    verPlaylists(user,objeto)
    cantPlaylist=objeto.user_playlists(user)["total"]
    if cantPlaylist != 0:
        opcion = validarEnteros("Elija la playlist cuyos tracks desea ver?(Nro): ")
    while opcion>cantPlaylist or opcion<=0:
        print("El numero ingresado no corresponde a ninguna playlist.")
        opcion = validarEnteros('Elija la playlist cuyos tracks desea ver?(Nro): ')
    if opcion <= cantPlaylist and opcion > 0:
        plid = objeto.user_playlists(user)['items'][opcion-1]['id']
        verPlaylistsTracks(user,objeto,plid)
    input("Ingrese enter para volver al menu...")
    
def crearPlaylist(user,objeto):
    """Ingresa la URI del USER y el objeto de SPOTIPY
    Crea una playlist pública"""
    bandera1 = True
    bandera2 = False
    while bandera1:
        nombrePL = input("Ingrese el nombre que desee (X para salir): ")
        if nombrePL == 'x' or nombrePL == 'X':
            bandera1 = False
        else:
            bandera2 = True
            while bandera2:
                print(f'El nombre de la playlist será {nombrePL}')
                opcion = input('Desea cambiarlo? (SI/NO): ').lower()
                if opcion == 'si':
                    bandera2 = False
                elif opcion == 'no':
                    playlist = objeto.user_playlist_create(user,nombrePL, public=True)
                    print('Playlist creada con éxito.')
                    input('Presiona Enter para volver al menú...')
                    bandera2 = False
                    bandera1 = False
                else:
                    print('Ingrese un comando válido.')

def añadirCanciones(user,objeto):
    """Ingresa la URI del USER y el objeto de SPOTIPY
    Añade canciones a la playlist que se elija"""
    verPlaylists(user,objeto)
    cantplaylist=objeto.user_playlists(user)["total"]
    if cantplaylist != 0:
        opcion = validarEnteros('A qué playlist quiere añadir canciones?(Nro): ')
        while opcion>cantplaylist or opcion<=0:
            print("El numero ingresado no corresponde a ninguna playlist.")
            opcion = validarEnteros('A qué playlist quiere añadir canciones?(Nro): ')
        if opcion <= cantplaylist and opcion > 0:
            plid = objeto.user_playlists(user)['items'][opcion-1]['id']
            bandera = True
            while bandera:
                q = input('Ingrese la canción que desesa añadir a la playlist (X para finalizar): ').lower()
                if q == 'x':
                    bandera = False
                else:
                    listaTracks = objeto.search(q,limit=5,type='track',market="AR")
                    if len(listaTracks["tracks"]["items"])== 0:
                        print("No se han encontrado tracks con el nombre", q ,".")
                    else:
                        tracksEncontrados=[]
                        listaTuri= []
                        print("~Estos son los resultados de su busqueda: ")
                        for tracks in range(0,len(listaTracks["tracks"]["items"])):
                            infoTrack=(listaTracks["tracks"]["items"][tracks]["name"],listaTracks["tracks"]["items"][tracks]["artists"][0]["name"])
                            tracksEncontrados.append(infoTrack)
                            print(tracks+1,"-",tracksEncontrados[tracks])
                            turi=listaTracks['tracks']['items'][tracks]['uri']
                            listaTuri.append(turi)
                        opcionTrack=validarEnteros("Ingrese la cancion que desea añadir a la playlist (Nro), si no desea añadir ninguna ingrese 0:")
                        while opcionTrack>5 or opcionTrack<0:
                            print("El track elejido no es valido.")
                            opcionTrack=validarEnteros("Ingrese la cancion que desea añadir a la playlist (Nro), si no desea añadir ninguna ingrese 0:")
                        if opcionTrack!=0:
                            objeto.user_playlist_add_tracks(user,plid,[listaTuri[opcionTrack-1]])
                            

def eliminarCanciones(user,objeto):
    """Ingresa la URI del USER y el objeto de SPOTIPY
    Elimina canciones de la playlist que se elija"""
    verPlaylists(user,objeto)
    cantplaylist=objeto.user_playlists(user)["total"]
    if cantplaylist!=0:
        opcion = validarEnteros('A qué playlist quiere quitarle canciones?(Nro): ')
        while opcion>cantplaylist or opcion<=0:
            print("El numero ingresado no corresponde a ninguna playlist.")
            opcion = validarEnteros('A qué playlist quiere quitarle canciones?(Nro): ')
            print()
        if opcion <= cantplaylist and opcion > 0:
            plid = objeto.user_playlists(user)['items'][opcion-1]['id']
            playlistTracks=objeto.user_playlist_tracks(user,plid,limit=100, market="AR")
            verPlaylistsTracks(user,objeto,plid)
            if len(playlistTracks["items"])!=0:
                listaIdTracks=tracksId(user,objeto,plid)
                opcionTrack=validarEnteros("Ingrese la cancion que desea eliminar de la playlist (Nro), si no desea eliminar ninguna ingrese 0:")
                while opcionTrack>len(playlistTracks["items"]) or opcionTrack<0:
                    print("El track elejido no es valido.")
                    opcionTrack=validarEnteros("Ingrese la cancion que desea eliminar de la playlist (Nro), si no desea eliminar ninguna ingrese 0:")
                if opcionTrack != 0:
                    trackRemovido=listaIdTracks.pop(opcionTrack-1)
                    playlistRemovida=objeto.user_playlist_remove_all_occurrences_of_tracks(user, plid, [trackRemovido])
                    print("La cancion ha sido removida con éxito.")
                    input("Presione Enter para volver al Menú...")
                    
def ordenarPlaylist(user,objeto):
    """Ingresa la URI del USER y el objeto de SPOTIPY
    Crea un archivo csv con el NOMBRE, ALBUM y el ARTISTA
    ordena según elija el usuario"""
    print('ATENCIÓN. El archivo que quiere crear reemplazará al anterior.')
    continuar = input('Está seguro de que desea continuar?(SI/NO): ').lower()
    flag = True
    while flag:
        if continuar == 'si':
            flag = False
            listaGral = []
            verPlaylists(user,objeto)
            cantplaylist=objeto.user_playlists(user)["total"]
            if cantplaylist != 0:
                opcion = validarEnteros('Qué playlist desea ordenar?(Nro): ')
                while opcion>cantplaylist or opcion<=0:
                    print("El numero ingresado no corresponde a ninguna playlist.")
                    opcion = validarEnteros('Qué playlist desea ordenar?(Nro): ')
                if opcion <= cantplaylist and opcion > 0:
                    plid = objeto.user_playlists(user)['items'][opcion-1]['id']
                    tracks = objeto.user_playlist_tracks(user, plid,limit=100, market="AR")
                    
                    for item in tracks['items']:
                        name = item["track"]["name"]
                        album = item["track"]["album"]["name"]
                        artist = item["track"]["artists"][0]["name"]
                        lista = [name,album,artist]
                        listaGral.append(lista)
                    
                    print("Como quiere ordenar la playlist?(Nro)")
                    print("1- Ordenar por canción")
                    print("2- Ordenar por album")
                    print("3- Ordenar por artista")
                    opcion = input('Elija una opción: ')
                    
                    bandera = True
                    while bandera:
                        if opcion == "1":
                            bandera = False
                            listaGral.sort(key = lambda nombre: nombre[0])
                        elif opcion == "2":
                            bandera = False
                            listaGral.sort(key = lambda album: album[1])
                        elif opcion == "3":
                            bandera = False
                            listaGral.sort(key = lambda artista: artista[2])
                        else:
                            print("Opción inválida.")
                            opcion = input('Elija una opción: ')
                    
                    with open('mi_lista_ordenada.csv','w',encoding = "utf-8") as archivo:
                        manejadorcsv = csv.writer(archivo)
                        manejadorcsv.writerows(listaGral)
                            
                    print("El archivo 'mi_lista_ordenada.csv' se ha creado con éxito")
                    input("Presione Enter para volver al Menú...")
        elif continuar == 'no':
              flag = False
        else:
              print("La opción ingresada es inválida.")
              print('ATENCIÓN. El archivo que quiere crear reemplazará al anterior.')
              continuar = input('Está seguro de que desea continuar?(SI/NO): ').lower() 
        
def rankingPlaylist(user,objeto):
    """Ingresa la URI del USER y el objeto de SPOTIPY
    Abre el archivo 'playlist_grupos.txt' y ordena las
    playlists según la cantidad de seguidores"""
    archivo=open("playlist_grupos.txt","r")
    listaId=[]
    listaRanking=[]
    for linea in archivo:
        linea=linea.rstrip("\n")
        listaId.append(linea)
    archivo.close()
    for i in range(0,len(listaId)):
        jsonPlaylist=objeto.user_playlist(user,listaId[i])
        if listaId[i]=="0tTZuNvA5SIxIJURJYzG8z":
            tupla=(jsonPlaylist["followers"]["total"],"Hackerman: La playlist de los profes jaja altos lokis")
        else:    
            tupla=(jsonPlaylist["followers"]["total"],jsonPlaylist["name"])
        listaRanking.append(tupla)
    listaRanking.sort()
    listaRanking.reverse()
    for j in range(0,len(listaRanking)):
        print(listaRanking[j])
    input("Presione Enter para volver al Menú...")
def menu(user,objeto,keyOwm):
    bandera = True

    while bandera:
        try:
            print("~~~~~~~~~~~~~~~~~MENÚ~~~~~~~~~~~~~~~~~")
            print('1- Crear una playlist')
            print('2- Ver las playlists creadas')
            print('3- Agregar canciones a una playlist')
            print("4- Eliminar canciones de una playlist")
            print("5- Generar playlist según el clima")
            print("6- Mostrar top artistas de Argentina y Reino Unido")
            print("7- Ordenar playlist en un archivo csv")
            print("8- Ranking de playlists de Algoritmos I")
            print('0- Salir')
            opcion = input("Elija la opción que desea: ")

            if opcion == '1':
                crearPlaylist(user,objeto)
            
            elif opcion == '2':
                playlistsCreadas(user,objeto)
                
            elif opcion == '3':
                añadirCanciones(user,objeto)
                
            elif opcion == "4":
                eliminarCanciones(user,objeto)
            
            elif opcion =="5":
                generarPlaylistSegunClima(user,objeto,keyOwm)
            
            elif opcion =="6":
                topArgplid="37i9dQZEVXbMMy2roB9myp"
                topUKplid="37i9dQZEVXbLnolsZ8PSNw"
                print("El Top de artistas de Argentina es: ")
                topArtistasPais(user,objeto,topArgplid)
                print("El Top de artistas del Reino Unido es: ")
                topArtistasPais(user,objeto,topUKplid)
                input("Presione Enter para volver al Menú...")
                
            elif opcion =="7":
                ordenarPlaylist(user,objeto)
            
            elif opcion =="8":
                rankingPlaylist(user,objeto)
            
            elif opcion == '0':
                bandera = False
            
            else:
                print('Ingrese un comando valido.')
                
        except:
            print("Error de red, intentelo nuevamente")
            
    print("Hasta luego :)")
    
#PROGRAMA PRINCIPAL
sp = autorizacion()
menu(USER,sp,OWMKEY)
