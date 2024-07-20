from dotenv import load_dotenv
import os
from requests import post, get
import spotfiycalls as sc

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


token = sc.get_token()
result = sc.search_for_artist(token, "ACDC")
artist_id = (result["id"])
songs = sc.get_song_by_artist(token, artist_id)

for idx, song in enumerate(songs):
    print(f"{idx + 1}. {song['name']}")