from youtube import Youtube, Playlist, Search
from spotify import Spotify


yt: Youtube = Youtube()
yt_search: Search = Search(yt.youtube)
query_dict: dict = yt_search.search("Ali Avcıdan")
print(query_dict)

pl = Playlist = Playlist(yt.youtube, "PLDykUHIHZT8tTNNwCCSIOvdUxiUxFTQse")
print(pl.insert("rSJtx1p6vdY"))

sp: Spotify = Spotify()
print(sp.fetch_playlist_items_name("42r1I9gc1gscP0NQ9VBmEo"))

