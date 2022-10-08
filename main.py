from APIs.Google import create_service
from APIs.api import append_to_playlist

if __name__ == '__main__':
    CLIENT_FILE = "client_secret.json"
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube']
    service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)
    
    append_to_playlist(service, "PLDykUHIHZT8t-M0zH8qJjol4ms2p_mlCQ")