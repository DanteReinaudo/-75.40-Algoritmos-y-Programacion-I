import os
import sys
import json
import pyowm
import pprint
import spotipy
import spotipy.util as util

CID = "12a006cfd712418e86d2c660c6bb0b2e"
SECRET = "5f1db05c4d26454f8c4fd09209d4c150"
scope = "playlist-modify-public"
user = "ii4hjin5jvi883c76z6855plz"
redirect_uri = "https://www.google.com.ar/"

token = util.prompt_for_user_token(user,scope,CID,SECRET,redirect_uri)
if token:
    sp = spotipy.Spotify(auth=token)
    print(token)
else:
    print("No se pudo obtener el toke para el usuario", username)

"""def CrearPlaylist(user):
    nombre_playlist=input("Ingrese el nombre de la playliste que desea crear: ")
    infoplaylist=sp.user_playlist_create(user,nombre_playlist)
    playlistid=infoplaylist["id"]
    print(infoplaylist)
    print(playlistid)
    return(infoplaylist,playlistid)"""

def BuscarDatos():
    tipodato=input("Ingrese que tipo de dato esta buscando (Album, Artist, Track o Playlist): ").lower()
    while tipodato != "album" and tipodato != "artist" and tipodato != "track" and tipodato != "playlist":
        print("El tipo de dato ingresado no es valido, intentelo nuevamente")
        tipodato=input("Ingrese que tipo de dato esta buscando (Album,Artista,Track o Playlist): ").lower()
    busqueda=input("Ingrese el nombre del {0} que esta buscando: ".format(tipodato))
    infobusqueda=sp.search(busqueda,type=tipodato,market="AR")
    pprint.pprint(infobusqueda)



#info_playlist,playlist_id=CrearPlaylist(user)
BuscarDatos()