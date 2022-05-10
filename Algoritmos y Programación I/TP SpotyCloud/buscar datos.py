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


def BuscarTracks():
    nombre_track=input("Ingrese el nombre del track que esta buscando para añadir a su lista: ").lower()
    nombre_artista=input("Ingrese el nombre del artista del track {0}, si no sabe su nombre ingrese `0´: ".format(nombre_track)).lower() 
    if nombre_artista=="0":
        infobusqueda=sp.search(nombre_track,type=track,market="AR")
        pprint.pprint(infobusqueda)
    else:
        q=album:gold%20artist:abba
        infobusqueda=sp.search(q,type=track,market="AR")
        pprint.pprint(infobusqueda) 


BuscarDatos()