# SpoTube

## What is SpoTube
SpoTube is gets Spotify playlist track names, and adds to your Youtube playlist.

## API Usage

### Spotify
- Need a spotify developer account.
- Need a spotify application.

If you already created an application, SpoTube needs a ``client id`` and ``client secret``. 

### Youtube
- Need a google account.

First of all, open ``google cloud``.
- Go to ``Enabled APIs & services`` section.
- In ``Enabled APIs & services`` and go to ``ENABLE APIS AND SERVIVES``.
- Go to search, and input ``YouTube Data API v3``.
- Select ``YouTube Data API v3`` in 1 result.
- Click enable button.

## Modules Setup
### Youtube Search Python
``USAGE`` Search track name in Youtube.
```
pip install youtube-search-python
```
### Requests
``USAGE`` HTTP Library.
```
pip install requests
```
### Spotipy
``USAGE`` Get Spotify playlist track names.
```
pip install spotipy
```
### Google
``USAGE`` Use Google service
```
pip install --upgrade google-api-python-client
```
```
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
```
# License
This software is released under the [MIT](https://github.com/fsb3rke/SpoTube/blob/main/LICENSE) License.
