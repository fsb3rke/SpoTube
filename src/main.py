from youtube import Youtube, Playlist
from spotify import Spotify
import json
import time
import youtubesearchpython

def main():
    yt: Youtube = Youtube()
    sp: Spotify = Spotify()

    youtube_playlist_id = str(input("Please enter your Youtube Playlist Id: "))
    spotify_playlist_id = str(input("Please enter your Spotify Playlist Id: "))

    pl: Playlist = Playlist(yt.youtube, youtube_playlist_id)
    track_fetch_data = sp.fetch_playlist_items_name_with_artist_name(spotify_playlist_id)

    for track in track_fetch_data:
        # Search name in Youtube
        video_id = youtubesearchpython.VideosSearch(f"{track[0]} {track[1]}", limit=1).result()["result"][0]["id"]
        pl.insert(video_id=video_id)
        print(f"{video_id} has been inserted")
        time.sleep(1)

if __name__ == "__main__":
    main()