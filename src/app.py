import requests


class MusicBrainzClient:
    def __init__(self):
        self.base_url = "https://musicbrainz.org/ws/2"

    def search_artist(self, artist_name):
        url = f"{self.base_url}/artist"
        params = {
            "query": artist_name,
            "fmt": "json"
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            print("Error:", response.status_code)
            return []

        data = response.json()
        return data.get("artists", [])
