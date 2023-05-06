import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

class SpotifySong:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.sp = self._authenticate()

    def _authenticate(self):
        client_credentials_manager = SpotifyClientCredentials(self.client_id, self.client_secret)
        return spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def search_song(self, song_name, artist_name):
        results = self.sp.search(q='track:{} artist:{}'.format(song_name, artist_name), type='track')
        return results['tracks']['items'][0] if results['tracks']['items'] else None

    def get_song_data(self, song_name, artist_name):
        song_data = {}
        track_info = self.search_song(song_name, artist_name)

        if track_info:
            # Song name
            song_data['song_name'] = track_info['name']

            # Artist
            song_data['artist'] = track_info['artists'][0]['name']

            # Song ID
            song_data['song_id'] = track_info['id']

            # Number of streams
            song_data['num_streams'] = track_info['popularity']

            # Song duration
            song_data['duration_ms'] = track_info['duration_ms']

            # Song popularity
            song_data['popularity'] = track_info['popularity']

            # Other audio features
            features = self.sp.audio_features(tracks=[song_data['song_id']])[0]
            song_data['tempo'] = features['tempo']
            song_data['energy'] = features['energy']
            song_data['danceability'] = features['danceability']
            song_data['instrumentalness'] = features['instrumentalness']
            song_data['key'] = features['key']
            song_data['liveness'] = features['liveness']
            song_data['loudness'] = features['loudness']
            song_data['mode'] = features['mode']
            song_data['speechiness'] = features['speechiness']
            song_data['time_signature'] = features['time_signature']
            song_data['valence'] = features['valence']

        return song_data

    def get_song_data_batch(self, song_names, artist_names):
        song_data_list = []

        for song_name, artist_name in zip(song_names, artist_names):
            song_data = self.get_song_data(song_name, artist_name)
            song_data_list.append(song_data)

        return pd.DataFrame(song_data_list)




