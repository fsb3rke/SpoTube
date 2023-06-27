from youtube import Youtube, Playlist
from spotify import Spotify
import youtubesearchpython
import PySimpleGUI as sg
from threading import Thread


def handle_insert(pl: Playlist, track_fetch_data, window):
    ll = len(track_fetch_data)
    for i, track in enumerate(track_fetch_data):
        video_id = youtubesearchpython.VideosSearch(f"{track[0]} {track[1]}", limit=1).result()["result"][0]["id"]
        pl.insert(video_id)
        window["inserted_track_text"].update(f"{track[0]} | {track[1]}")
        window["total_inserted_track_text"].update(f" ({(i+1)}/{ll})")
        print(f"{track[0]} | {track[1]} => {video_id} ? INSERTED | ({(i+1)}/{ll})")
        
        # global stop_thread
        # if stop_thread:
            # break


def main():
    yt: Youtube = Youtube()
    sp: Spotify = Spotify()

    sg.theme("DarkAmber")

    layout = [
        [sg.Text("SpoTube")],
        [sg.Text("Youtube Playlist Id"), sg.InputText()],
        [sg.Text("Spotify Playlist Id"), sg.InputText()],
        [sg.Button("Convert")], #, sg.Button("Stop")],
        [sg.Text("fsb3rke", key="inserted_track_text"), sg.Text("0/0", key="total_inserted_track_text")]
    ]

    window = sg.Window("SpoTube", layout)

    while True:
        event, values = window.read()
        th = None

        if event == sg.WIN_CLOSED:
            break

        if event == "Convert":
            if not (values[0] == "" or values[1] == ""):
                pl: Playlist = Playlist(yt.youtube, values[0])
                track_fetch_data = sp.fetch_playlist_items_name_with_artist_name(values[1])

                # stop_thread = False
                th = Thread(target=handle_insert, args=(pl, track_fetch_data, window))
                th.start()

        # if event == "Stop":
            # if th is not None:
                # stop_thread = True
                # th.join()
                # th = None

            print(values)




if __name__ == "__main__":
    main()
