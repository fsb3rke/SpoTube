import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os


load_dotenv()

class Spotify:
    def __init__(self) -> None:
        self.__auth_manager = SpotifyClientCredentials(client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET"))
        self.__sp = spotipy.Spotify(auth_manager=self.__auth_manager)

    def fetch_playlist_items_name(self, playlist_id: str) -> list:
        playlist = self.__sp.playlist(playlist_id=playlist_id)
        tracks = playlist["tracks"]["items"]
        return [x["track"]["name"] for x in tracks]
