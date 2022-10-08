from requests import request
from youtubesearchpython import VideosSearch


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

playlist_link = "https://open.spotify.com/playlist/6GmeNx5cP9Uk2BzGNbCW4h?si=ddb5c4fa5a694a91"


# playlist_id = playlist_link.split("/")[::-1][0]

def get_track_names(playlist_id: str, client_id: str, client_secret: str) -> list:
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    track_names = [x["track"]["name"] for x in sp.playlist_tracks(playlist_id)["tracks"]["items"]]
    return track_names


spotify: dict = {"client_id": "999485233b684b27980dbad0c90b0a45",
                "client_secret": "10f3db73784e41d9836da4dee7509648"}

def get_video_ids() -> list:
    tracks = get_track_names("6GmeNx5cP9Uk2BzGNbCW4h?si=ddb5c4fa5a694a91",
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

