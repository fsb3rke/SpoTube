from youtube import Youtube, Playlist, Search

yt: Youtube = Youtube()
yt_search: Search = Search(yt.youtube)
query_dict: dict = yt_search.search("Ali Avcıdan")
print(query_dict)

pl = Playlist = Playlist(yt.youtube, "PLDykUHIHZT8tTNNwCCSIOvdUxiUxFTQse")
print(pl.insert("rSJtx1p6vdY"))