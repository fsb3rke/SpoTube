from youtube import Youtube, Playlist
from spotify import Spotify
import time
import youtubesearchpython
import PySimpleGUI as sg

def main():
    yt: Youtube = Youtube()
    sp: Spotify = Spotify()

    sg.theme("DarkAmber")

    layout = [
        [sg.Text("SpoTube")]
        [sg.Text("Youtube Playlist Id"), sg.InputText()],
        [sg.Text("Spotify Playlist Id"), sg.InputText()],
        [sg.Button("Ok")]
    ]

    window = sg.Window("SpoTube", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == "Ok":
            pl: Playlist = Playlist(yt.youtube, values[0])
            track_fetch_data = sp.fetch_playlist_items_name_with_artist_name(values[1])

            for track in track_fetch_data:
                # Search name in Youtube
                video_id = youtubesearchpython.VideosSearch(f"{track[0]} {track[1]}", limit=1).result()["result"][0]["id"]
                pl.insert(video_id=video_id)
                print(f"{video_id} has been inserted")

        print(values)




if __name__ == "__main__":
    main()