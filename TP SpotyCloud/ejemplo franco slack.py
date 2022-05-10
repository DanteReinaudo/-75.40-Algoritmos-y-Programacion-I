import spotipy
sp = spotipy.Spotify() 
from spotipy.oauth2 import SpotifyClientCredentials 
cid="12a006cfd712418e86d2c660c6bb0b2e"
secret = "5f1db05c4d26454f8c4fd09209d4c150"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
sp.trace=False