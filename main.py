from dotenv import load_dotenv
import os
from requests import post, get
import spotfiycalls as sc
from flask import Flask

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


token = sc.get_token()
artist_name = input('Which artist do you want to search? \nName:')
result = sc.search_for_artist(token, artist_name=artist_name)
artist_id = (result["id"])
songs = sc.get_song_by_artist(token, artist_id)

for idx, song in enumerate(songs):
    print(f"{idx + 1}. {song['name']}")