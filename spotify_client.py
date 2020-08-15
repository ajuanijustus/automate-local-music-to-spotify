import requests
import urllib.parse
import json


class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token

    def search_song(self, artist, track):
        query = urllib.parse.quote(f'{artist} {track}')
        url = f"https://api.spotify.com/v1/search?q={query}&type=track"
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        response_json = response.json()
        results = response_json['tracks']['items']
        if results:
            # let's assume the first track in the list is the song we want
            return results[0]['id']
        else:
            print("No song found for " + artist + " - " + track)
            pass

    def add_song_to_spotify(self, song_id, playlist_id):
        url = "https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks"
        song_id = 'spotify:track:' + song_id
        uris = [song_id]
        request_data = json.dumps(uris)
        response = requests.post(
            url,
            data=request_data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        return response.ok
