from APIs.Google import create_service
from APIs.api import append_to_playlist

if __name__ == '__main__':
    CLIENT_FILE = "client_secret.json"
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube']
    service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)
    
    playlist_id_input_youtube = str(input("Youtube Playlist Id: "))
    append_to_playlist(service, "youtube_playlist_id")