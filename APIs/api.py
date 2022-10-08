# Copyright (c) 2022 fsb3rke
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from requests import request
from youtubesearchpython import VideosSearch
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# playlist_id = playlist_link.split("/")[::-1][0] # parse link to get link id

def get_track_names(playlist_id: str, client_id: str, client_secret: str) -> list:
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    track_names = [x["track"]["name"] for x in sp.playlist_tracks(playlist_id)["tracks"]["items"]]
    return track_names


spotify: dict = {"client_id": "spotify_client_id",
                "client_secret": "spotify_client_secret"}

def get_video_ids() -> list:
    playlist_id_input_spotify = str(input("Spotify Playlist Id: "))
    tracks = get_track_names(playlist_id_input_spotify,
                            spotify["client_id"],
                            spotify["client_secret"])

    tracks_ids: list = []
    for i in tracks:
        video = VideosSearch(i, limit = 1)
        video_id = video.result()["result"][0]["id"]
        tracks_ids.append(video_id)
    
    return tracks_ids

def append_to_playlist(service_instance, target_playlist: str) -> None:
    videos = get_video_ids()
    if not videos:
        print("Source playlist is empty")
        return
    for i in videos:
        request_body = {
            'snippet': {
                'playlistId': target_playlist,
                'resourceId': {
                    'kind': 'youtube#video',
                    'videoId': i
                }
            }
        }
        print(f"{i}")
        service_instance.playlistItems().insert(
            part='snippet',
            body=request_body
        ).execute()
    print("Process complete.")

