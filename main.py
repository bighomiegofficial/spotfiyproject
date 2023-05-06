from spotify_api import SpotifySong

def get_data():
    client_id = "45a9d1ebfcc34203bf0a849a317e486c"
    client_secret = "48886900a84a458884c437a0aa26e328"
    spotify_song = SpotifySong(client_id, client_secret)
    song_names = ["Shape of You", "Blinding Lights", "Strike (Holster)"]
    artist_names = ["Ed Sheeran", "The Weeknd", "Lil Yachty"]
    song_data_df = spotify_song.get_song_data_batch(song_names, artist_names)

    return song_data_df


if __name__ == '__main__':
    song_data = get_data()
    song_data.to_csv('C:/Users/Admin/PycharmProjects/spotifyproject/data/song_data.csv')

