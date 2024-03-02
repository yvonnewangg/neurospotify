import requests
import datetime
import geocoder
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# # Set your Spotify app credentials (client ID and client secret)
# client_id = 'ee2e90dfb2f2444899478ef603544c90'
# client_secret = '4b5e1351ff7f461b8a3d9f2bf570e3a2'
# redirect_uri = 'http://localhost:3000/callback'

# # scopes for Remote control playback, Get Available Devices, Pause playback
# SCOPEs = ['app-remote-control', 'user-read-playback-state',
#           'user-modify-playback-state']


# def pause_spotify():
#     devices = sp.devices()
#     print(devices)
#     for device in devices['devices']:
#         if device['is_active']:
#             print("is active")
#             sp.pause_playback(device['id'])


# def resume_spotify():
#     devices = sp.devices()
#     for device in devices['devices']:
#         if device['is_active']:
#             sp.start_playback(device['id'])


# def main():
#     print(sp.current_user_followed_artists())
#     resume_spotify()
#     pause_spotify()


# if __name__ == '__main__':
#     auth_manager = SpotifyOAuth(
#         client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=SCOPEs)
#     sp = spotipy.Spotify(auth_manager=auth_manager)
#     main()

# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify(
#     client_credentials_manager=SpotifyClientCredentials())


# spotify.devices()

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep


# def start_song():
#     scope = "user-read-playback-state,user-modify-playback-state"
#     sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

#     # Shows playing devices
#     res = sp.devices()
#     print(res)

#     sp.start_playback(uris=['spotify:track:6gdLoMygLsgktydTQ71b15'])

#     sp.volume(100)
#     sleep(2)
#     sp.volume(50)
#     sleep(2)
#     sp.volume(100)

#     sp.pause_playback()

Active = False


def play_or_pause():
    global Active
    scope = "user-read-playback-state,user-modify-playback-state"
    sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

    if Active == False:
        sp.start_playback(
            context_uri='spotify:playlist:37i9dQZF1DXcBWIGoYBM5M')
        Active = not (Active)
    else:
        sp.pause_playback()
        Active = not (Active)


def skip():
    scope = "user-read-playback-state,user-modify-playback-state"
    sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))
    sp.next_track()


play_or_pause()

sleep(5)
skip()
sleep(5)
play_or_pause()
