import json
from pyowm import OWM
import spotipy
import spotipy.util as util

SCOPE = 'playlist-modify-public'
CLIENTID = '12a006cfd712418e86d2c660c6bb0b2e'
SECRETID = '5f1db05c4d26454f8c4fd09209d4c150'
RED_URI = 'https://www.google.com.ar/'
USER = 'ii4hjin5jvi883c76z6855plz'
OWMKEY="ab80e05035de9a636ccca6c4250dfa6d"

#Genera el TOKEN
def autorizacion():
    token = util.prompt_for_user_token(USER,SCOPE,CLIENTID,SECRETID,RED_URI)
    objeto = spotipy.Spotify(auth=token)
    return objeto

def keyOwm(key):
    "pide la key de la api y devuelve el objeto owm"
    objeto = OWM(key)
    return(objeto)

def obtenerClima():
    pass
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

def verPlaylistsTracks(user,objeto,playlistId):
    "muestra los tracks de una playlist"
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
    cantPlaylist = len(objeto.user_playlists(USER)['items'])
    if cantPlaylist != 0:
        for i in range(cantPlaylist):
            print(str(i+1) + '- ' + str(objeto.user_playlists(user)['items'][i]['name']))
    else:
        print('No hay playlists creadas.')
        
def playlistsCreadas(user,objeto):
    "muestra las playlist, permite elejir una y muestra los tracks de la playlist"
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

def menu(user,objeto):
    bandera = True

    while bandera:
        print("~~~~~~~~~~~~~~~~~MENÚ~~~~~~~~~~~~~~~~~")
        print('1- Crear una playlist')
        print('2- Ver las playlists creadas')
        print('3- Agregar canciones a una playlist')
        print("4- Eliminar canciones de una playlist")
        print("5- Generar playlist según el clima")
        print("6- Mostrar top artistas de Londres y Buenos Aires")
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
            pass
        
        elif opcion =="6":
            pass
        
        elif opcion =="7":
            pass
        
        elif opcion =="8":
            pass
        
        elif opcion == '0':
            bandera = False
        
        else:
            print('Ingrese un comando valido.')
    print("Hasta luego :)")
    
#PROGRAMA PRINCIPAL
sp = autorizacion()
owm = keyOwm(OWMKEY)
menu(USER,sp)

"""
estas son las líneas para abrir
el Json en un archivo .txt

json_lista = json.dumps(plid, indent=2)
temp = open("temp.txt","w")
temp.write(json_lista)
temp.close()
"""