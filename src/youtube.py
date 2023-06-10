import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import json
import random


def quick_dump(response: str) -> dict:
    return json.dumps(response, indent=2)

class Youtube:
    def __init__(self) -> None:
        self.__scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
        self.__api_service_name = "youtube"
        self.__api_version = "v3"
        self.__client_secret_file = "client_secret.json"

        self.__flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file=self.__client_secret_file,
            scopes=self.__scopes
        )

        self.__credentials = self.__flow.run_local_server(port=random.randint(1000, 10000)) # 1000 - 9999
        self.youtube = googleapiclient.discovery.build(
            serviceName=self.__api_service_name,
            version=self.__api_version,
            credentials=self.__credentials
        )


class Search:
    def __init__(self, yt) -> None:
        self.yt = yt

    def search(self, query_name: str) -> dict:
        query_request = self.yt.search().list(
            part="snippet",
            maxResults=1,
            q=query_name
        )
        query_response = query_request.execute()
        
        return quick_dump(query_response)


# ROAD_MAP : 
#           - Remove(video_id: str)
#           - List()
#             Create(playlist_name: str) -> returns playlist_id
class Playlist:
    def __init__(self, yt, playlist_id: str) -> None:
        self.yt = yt
        self.id = playlist_id

    def insert(self, video_id: str) -> dict:
        insert_request = self.yt.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": self.id,
                    "position": 0,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id
                    }
                }
            }
        )

        response = insert_request.execute()
        return quick_dump(response)



