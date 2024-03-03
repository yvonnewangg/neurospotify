import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep

Active = False
First = False


def play_or_pause():
    global Active
    global First
    scope = "user-read-playback-state,user-modify-playback-state"
    sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

    if Active == False:
        if not First:
            sp.start_playback(
                context_uri='spotify:playlist:37i9dQZF1DXcBWIGoYBM5M')
            First = True
        else:
            sp.start_playback()
        Active = not Active
    else:
        sp.pause_playback()
        Active = not Active


def skip():
    scope = "user-read-playback-state,user-modify-playback-state"
    sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))
    sp.next_track()


def prev_song():
    scope = "user-read-playback-state,user-modify-playback-state"
    sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))
    sp.previous_track()
