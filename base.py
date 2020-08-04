import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import sys, os, time, serial

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

serial = serial.Serial('COM3', 9600)
token = util.prompt_for_user_token(username='r1cjzwkjtbzb0up9vk270d7kj?si=lcJUEfHySMWKYDdVDUQ4Pg',client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri='http://roblburris.com/', scope='user-read-playback-state')
sp = spotipy.Spotify(auth=token)

user = sp.current_user()
results = sp.current_playback(market=None)
print(results['item']['name'])

prev_sa = {}
prev_sa[results['item']['name']] = results['item']['album']['artists'][0]['name']

while True:
    results = sp.current_playback(market=None)
    song_artist = {}
    song_artist[results['item']['name']] = results['item']['album']['artists'][0]['name']
    cur = results['item']['name']
    if ("(" or " -") in cur:
        if "(" in cur:
            cur = cur[0:cur.index('(')]
        else:
            cur = cur[0:cur.index(' -')]
    cur = cur.encode('ascii',errors='ignore')
    cur = cur.decode().strip()
    if len(cur) > 16:
        for i in range(15, -1, -1):
            if cur[i] == ' ':
                cur = cur[0 : i] + "    " + cur[i + 1 : len(cur)]
                break
    else:
        cur += "    " + results['item']['album']['artists'][0]['name']
    
    serial.write(cur.encode())

    if prev_sa != song_artist:
        print(results['item']['name'] + " - " + results['item']['album']['artists'][0]['name'])
        prev_sa = song_artist
    
    time.sleep(1)
    
