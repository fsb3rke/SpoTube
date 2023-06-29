from youtube import Youtube, Playlist
from spotify import Spotify
import youtubesearchpython
import PySimpleGUI as sg
from threading import Thread


MAX_CHARACTER_LIMIT = 40

def is_empty(x: str) -> bool:
    return x == ""

def handle_character_limit(x: str) -> str:
    return x[:MAX_CHARACTER_LIMIT]

class Raiser:
    def __init__(self):
        self.stop_thread = False

def handle_convert(window, values, sp, yt, max_number_of_insert_track, raiser) -> None:
    pl: Playlist = Playlist(yt.youtube, values[0])
    window["inserted_track_text"].update("Fetching Spotify Playlist...")
    track_fetch_data = sp.fetch_playlist_items_name_with_artist_name(values[1])
    ll = len(track_fetch_data)
    int_max_number_of_insert_track = int(max_number_of_insert_track)
    int_max_number_of_insert_track = ll if int_max_number_of_insert_track > ll else 1 if int_max_number_of_insert_track < 1 else int_max_number_of_insert_track

    try:
        for i, track in enumerate(track_fetch_data):
            video_id = youtubesearchpython.VideosSearch(f"{track[0]} {track[1]}", limit=1).result()["result"][0]["id"]
            pl.insert(video_id)
            window["inserted_track_text"].update(f"{handle_character_limit(track[0])} | {track[1]}")
            window["total_inserted_track_text"].update(f" ({(i+1)}/{int_max_number_of_insert_track})")
            print(f"{track[0]} | {track[1]} => {video_id} ? INSERTED | ({(i+1)}/{int_max_number_of_insert_track})")

            if (i+1) >= int_max_number_of_insert_track: # Why this is happening idk. It recongnized str instead of int.
                break
            
            elif raiser.stop_thread:
                break
    except RuntimeError:
        pass

def main():
    yt: Youtube = Youtube()
    sp: Spotify = Spotify()

    sg.theme("DarkAmber")

    layout = [
        [sg.Text("SpoTube")],
        [sg.Text("Youtube Playlist Id"), sg.Push(), sg.InputText()],
        [sg.Text("Spotify Playlist Id  "), sg.Push(), sg.InputText()],
        [sg.Text("Max Number of Insert Track"), sg.InputText()],
        [sg.Button("Convert"), sg.Button("Stop")],
        [sg.Text("fsb3rke", key="inserted_track_text"), sg.Push(), sg.Text("0/0", key="total_inserted_track_text")]
    ]

    window = sg.Window("SpoTube", layout)
    th = [None]
    raiser = Raiser()

    while True:
        event, values = window.read()
        youtube_playlist_id, spotify_playlist_id, max_number_of_insert_track = values[0], values[1], values[2]

        if event == sg.WIN_CLOSED:
            break

        if event == "Convert":
            if not (is_empty(youtube_playlist_id) or is_empty(spotify_playlist_id)):

                th[0] = Thread(target=handle_convert, args=(window, values, sp, yt, max_number_of_insert_track, raiser))
                th[0].start()
                
                raiser.stop_thread = False

        if event == "Stop":
            print("Stop Button Pressed")
            raiser.stop_thread = True
            th[0].join()
            raiser.stop_thread = False
            window["inserted_track_text"].update("fsb3rke")
            window["total_inserted_track_text"].update("0/0")

            print(values) # , stop_thread)




if __name__ == "__main__":
    main()
