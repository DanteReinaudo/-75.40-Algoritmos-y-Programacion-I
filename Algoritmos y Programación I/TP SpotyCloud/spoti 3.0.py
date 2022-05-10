import json
import time
import spotipy
import spotipy.util as util
from pyowm import OWM
from random import randrange
from collections import OrderedDict

SCOPE = 'playlist-modify-public'
CLIENTID = '12a006cfd712418e86d2c660c6bb0b2e'
SECRETID = '5f1db05c4d26454f8c4fd09209d4c150'
RED_URI = 'https://www.google.com.ar/'
USER = 'ii4hjin5jvi883c76z6855plz'
OWMKEY="ab80e05035de9a636ccca6c4250dfa6d"

#Genera el TOKEN
def autorizacion():
    "funcion para poder trabajon con la Api Spotipy, valida el usuario y devuelve objeto para trabajar"
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
    "funcion para poder trabajar con la Api pyOWM pide la key de lusuario y devuelve objeto para trabajar."
    objeto = OWM(key)
    return(objeto)

def obtenerClima(key):
    "La funcion recibe la keyOwm, devuelve tupla hora/fecha, el porcentaje de nubes y la temperatura en C"
#    lugar=objeto.weather_at_coords(-34.61, -58.38)
    owm=keyOwm(key)
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
    "Saca el id de los tracks de una playlist, los devuelve en lista"
    playlistTracks=objeto.user_playlist_tracks(user, playlistId,limit=100, market="AR")
    listaId=[]
    if len(playlistTracks["items"]) != 0:
        for tracks in range(0,len(playlistTracks["items"])):
            trackId=playlistTracks["items"][tracks]["track"]["id"]
            listaId.append(trackId)
    return(listaId)

def generarListaDeTracks(user,objeto,listaPlaylist):
    """recibe una lista con el id de varias playlist y devuelve una lista mas grande con todos los tracks.
       une los tracks de varias playlsit."""
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
            
    elif nubes<60 and temperatura>19 and len(lluvias)==0:
        activoPlaylistID=["37i9dQZF1DX0hWmn8d5pRe","37i9dQZF1DXadOVCgGhS7j","37i9dQZF1DX9ZKyQHcEFXZ"]
        activoTracks=generarListaRandom(user,objeto,activoPlaylistID)
        objeto.user_playlist_add_tracks(user,plidClima,activoTracks)
            
    elif len(lluvias)==0 and int(tiempo[0][0])==0 and int(tiempo[0][1]) <= 7:
        joditaPlaylistID=["37i9dQZF1DWUlCmB8llCTB","37i9dQZF1DWZjqjZMudx9T","37i9dQZF1DWTkIwO2HDifB","37i9dQZF1DXdMS2nFQ7EO0"]
        joditaTracks=generarListaRandom(user,objeto,joditaPlaylistID)
        objeto.user_playlist_add_tracks(user,plidClima,joditaTracks)
        
    else:
        print("El clima no coincide con los parametros dados")

def topArtistasPais(user,objeto,plid):
    "Recibe la id de la playlist top 50 de algun pais, imprime los artistas cuya popularidad es mayor a 90, No devuelve nada"
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
    "recibe la id de una playlist y muestra sus tracks, si no tiene imprime que no hay tracks. No devuelve nada"
    playlistTracks=objeto.user_playlist_tracks(user, playlistId,limit=100, market="AR")
    if len(playlistTracks["items"])== 0:
        print("La playlist no tiene ningun track.")
    else:
        print("Estos son los tracks de la playlist: ")
        for tracks in range(0,len(playlistTracks["items"])):
            infoTrack=(playlistTracks["items"][tracks]["track"]["name"],playlistTracks["items"][tracks]["track"]["artists"][0]["name"])
            print(tracks+1,"-",infoTrack)
            
#Ingresa la URI del USER y el objeto de SPOTIPY
#Muestra las playlists ya creadas
def verPlaylists(user,objeto):
    "Muestra las playlist de un usuario. No devuelve nada"
    cantPlaylist = len(objeto.user_playlists(USER)['items'])
    if cantPlaylist != 0:
        for i in range(cantPlaylist):
            print(str(i+1) + '- ' + str(objeto.user_playlists(user)['items'][i]['name']))
    else:
        print('No hay playlists creadas.')
        
def playlistsCreadas(user,objeto):
    "muestra las playlist, permite elejir una y muestra los tracks de la playlist, no devuelve nada"
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
#Ingresa la URI del USER y el objeto de SPOTIPY
#Crea una playlist pública
def crearPlaylist(user,objeto):
    "Permite crear una playlist, elegir su nombre y no devuelve nada."
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
        
#Ingresa la URI del USER y el objeto de SPOTIPY
#Añade canciones a la playlist que se elija
def añadirCanciones(user,objeto):
    "permite añadir canciones a una playlist a eleccion, buscar la cancion y elejir entre las primeras 5 busquedas,  no devuelve nada"
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
    "Permite elejir una playlis y eliminar una cancion, no devuelve nada"
    verPlaylists(user,objeto)
    cantplaylist=objeto.user_playlists(user)["total"]
    if cantplaylist!=0:
        opcion = validarEnteros('A qué playlist quiere quitarle canciones?(Nro): ')
        while opcion>cantplaylist or opcion<=0:
            print("El numero ingresado no corresponde a ninguna playlist.")
            opcion = validarEnteros('A qué playlist quiere quitarle canciones?(Nro): ')
        if opcion <= cantplaylist and opcion > 0:
            plid = objeto.user_playlists(user)['items'][opcion-1]['id']
            playlistTracks=objeto.user_playlist_tracks(user,plid,limit=100, market="AR")
            verPlaylistsTracks(user,objeto,plid)
            listaIdTracks=tracksId(user,objeto,plid)
            opcionTrack=validarEnteros("Ingrese la cancion que desea eliminar de la playlist (Nro), si no desea eliminar ninguna ingrese 0:")
            while opcionTrack>len(playlistTracks["items"]) or opcionTrack<0:
                print("El track elejido no es valido.")
                opcionTrack=validarEnteros("Ingrese la cancion que desea eliminar de la playlist (Nro), si no desea eliminar ninguna ingrese 0:")
            if opcionTrack != 0:
                trackRemovido=listaIdTracks.pop(opcionTrack-1)
                playlistRemovida=objeto.user_playlist_remove_all_occurrences_of_tracks(user, plid, [trackRemovido])

def rankingPlaylist(user,objeto):
    archivo=open("playlist_grupos.txt","r")
    linea=archivo.readline()
    print(linea)
    json=objeto.user_playlist(user,"2ukWk6zLIukX8On1tWtvnN")
    print(json["followers"]["total"])
    archivo.close()
    
def menu(user,objeto,keyOwm):
    "Menu, permite al usuario elejir que desea hacer, no devuelve nada"
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
            print("7- Ordenar playlist")
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
            
            elif opcion =="7":
                pass
            
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

"""
estas son las líneas para abrir
el Json en un archivo .txt

json_lista = json.dumps(plid, indent=2)
temp = open("temp.txt","w")
temp.write(json_lista)
temp.close()
"""