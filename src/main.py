from youtube import Youtube, Playlist
from spotify import Spotify
import youtubesearchpython
import PySimpleGUI as sg
from threading import Thread


stop_thread = [False] # manipulate pointer

def handle_insert(pl: Playlist, track_fetch_data, window, max_number_of_insert_track):
    ll = len(track_fetch_data)
    for i, track in enumerate(track_fetch_data):
        video_id = youtubesearchpython.VideosSearch(f"{track[0]} {track[1]}", limit=1).result()["result"][0]["id"]
        pl.insert(video_id)
        window["inserted_track_text"].update(f"{track[0]} | {track[1]}")
        window["total_inserted_track_text"].update(f" ({(i+1)}/{ll})")
        print(f"{track[0]} | {track[1]} => {video_id} ? INSERTED | ({(i+1)}/{ll})")

        if (i+1) == max_number_of_insert_track:
            break
        
        
        if stop_thread[0]:
            break


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

    while True:
        event, values = window.read()
        youtube_playlist_id, spotify_playlist_id, max_number_of_insert_track = values[0], values[1], values[2]
        th = None

        if event == sg.WIN_CLOSED:
            break

        if event == "Convert":
            if not (youtube_playlist_id == "" or spotify_playlist_id == ""):
                pl: Playlist = Playlist(yt.youtube, values[0])
                track_fetch_data = sp.fetch_playlist_items_name_with_artist_name(values[1])
                int_max_number_of_insert_track = int(max_number_of_insert_track)
                int_max_number_of_insert_track = len(track_fetch_data) if int_max_number_of_insert_track > len(track_fetch_data) else 1 if int_max_number_of_insert_track < 1 else int_max_number_of_insert_track


                # stop_thread = False
                th = Thread(target=handle_insert, args=(pl, track_fetch_data, window, int_max_number_of_insert_track))
                th.start()

        if event == "Stop":
            if th is not None:
                stop_thread[0] = True
                th.join()
                th = None

            print(values) # , stop_thread)




if __name__ == "__main__":
    main()
