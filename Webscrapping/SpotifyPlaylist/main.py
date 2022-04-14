# -*- coding: utf-8 -*-
"""
  Created on Fri Mar 25 15:41:47 2022

@author: DELL
"""

import requests 
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

clientId = os.environ['Spotify_clientId']
clientSecret = os.environ['Spotify_clientSecret']
list_songs = []

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientId,
                                               client_secret=clientSecret,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="playlist-modify-public"))
date = input("Enter the date to get top 100 trending songs of that week.(format - yyyy-mm-dd)")
playlist = input("Enter the name of the playlist that you wish to create")

r = requests.get(url = "https://www.billboard.com/charts/hot-100/"+date)
   
soup = BeautifulSoup(r.content, 'html.parser')
   
track_names = soup.find_all('h3', attrs = {"class":"c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only","id":"title-of-a-story"}) 
track_artist = soup.find_all('span',attrs = {"class":"c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"})

for i,j in zip(track_names,track_artist):
    song_name = i.string
    artist_name = j.string
    artist_name = artist_name.replace("\n","")
    artist_name =artist_name.replace("\t","")
    song_name = song_name.replace("\n","")
    song_name =song_name.replace("\t","")
    track_id = sp.search(q='artist:' + artist_name + ' track:' + song_name, type='track')
    if track_id['tracks']['total'] == 0: #if track isn't on spotify as queried, go to next track
        continue
    list_songs.append(track_id['tracks']['items'][0]['id'])

sp.user_playlist_create("31dxa3ixcph5gmmhylkj2zbuph6i",playlist,public = True,collaborative = False)
sp.playlist_add_items(playlist_id = "3paKB6UTtQ0IiJDYkxowcv",items = list_songs)