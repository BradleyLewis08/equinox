# Import libraries
import os
import sys
import json
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests


def authenticate():
    username = "cn5jjcibmzjy628o0srxs9tzf"
    scope = 'user-read-private streaming user-read-playback-state user-modify-playback-state'
    redirect_uri = "https://www.google.com"
    CLIENT_ID = '8eb38b719b8e40a9b4b9b67d67728356'
    CLIENT_SECRET = 'a3bfa4e95428427980c48227201c9003'
    token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, redirect_uri)
    sp = spotipy.Spotify(auth=token)
    return sp

sp = authenticate()

def play_track(track_name):
    query = 'track:'+ track_name
    tracks = sp.search(q=query, limit = 1)
    track_uri = tracks["tracks"]["items"][0]["uri"]
    album_uri = tracks["tracks"]["items"][0]["album"]["uri"]
    sp.start_playback(device_id=None, context_uri=album_uri, offset={"uri": track_uri})
    try:
        sp.volume(90)
    except:
        print("Volume control disallowed on this device.")
    
def pause_track():
    if sp.currently_playing():
        sp.pause_playback()
    else:
        print("I'm not playing anything right now.")


"""
Debugging
devices = sp.devices()
print(json.dumps(devices, sort_keys=True, indent=4))
print(json.dumps(tracks, sort_keys=True, indent=4))
"""