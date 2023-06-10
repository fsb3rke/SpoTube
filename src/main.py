from youtube import Youtube, Playlist, Search
from spotify import Spotify
import json


def main():
    yt: Youtube = Youtube()
    yt_search: Search = Search(yt.youtube)
    sp: Spotify = Spotify()

    youtube_playlist_id = str(input("Please enter your Youtube Playlist Id: "))
    spotify_playlist_id = str(input("Please enter your Spotify Playlist Id: "))

    pl: Playlist = Playlist(yt.youtube, youtube_playlist_id)
    track_names = sp.fetch_playlist_items_name(spotify_playlist_id)

    for name in track_names:
        # Search name in Youtube
        video_id = json.loads(yt_search.search(name))["items"][0]["id"]["videoId"]
        pl.insert(video_id=video_id)

if __name__ == "__main__":
    main()