import spotipy
import os
from spotipy import util
usuario="ii4hjin5jvi883c76z6855plz"
ID_CLIENTE="12a006cfd712418e86d2c660c6bb0b2e"
ID_SECRET="5f1db05c4d26454f8c4fd09209d4c150"
try:
    token = util.prompt_for_user_token(usuario,"user-library-read",client_id=ID_CLIENTE,client_secret=ID_SECRET,redirect_uri='http://localhost:8888/callback')
except:
    os.remove(f".cache-{usuario}")
    token = util.prompt_for_user_token(usuario,"user-library-read",client_id=ID_CLIENTE,client_secret=ID_SECRET,redirect_uri='http://localhost:8888/callback')
​
if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print( track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print( "Can't get token for", usuario)
​
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(auth=token)
results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])
​
for album in albums:
    print(album['name'])