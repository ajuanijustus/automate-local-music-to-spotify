import os
import pandas as pd
import eyed3

from spotify_client import SpotifyClient


def song_info(path):
    audiofile = eyed3.load(path)
    song = {}
    try:
        song['artist'] = audiofile.tag.artist
    except:
        song['artist'] = None
    try:
        song['track'] = audiofile.tag.title
    except:
        song['track'] = None
    return song

def run():

    spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
    main_music_folder = os.getenv('DIR_MUSIC')
    playlist_id = os.getenv('PLAYLIST_ID')

    os.chdir(main_music_folder)
    song_list = []
    for root, dirs, files in os.walk(main_music_folder, topdown=True):
        for name in files:
            if name.endswith('.mp3'):
                song_list.append(os.path.join(root, name))

    songs = pd.DataFrame(song_list, columns=['path'])
    songs['song_info'] = songs['path'].apply(lambda x: song_info(x))
    songs[['artist', 'track']] = songs['song_info'].apply(pd.Series)
    songs = songs[~((songs['artist'].isin([None, ' ', ''])) | (songs['track'].isin([None, ' ', ''])))].reset_index(drop=True)
    songs = songs['song_info'].tolist()

    for song in songs:
        spotify_song_id = spotify_client.search_song(song['artist'], song['track'])
        if spotify_song_id:
            added_song = spotify_client.add_song_to_spotify(spotify_song_id, playlist_id)
            if added_song:
                print(f"Added {song['artist']} - {song['track']} to your Spotify Playlist.")


if __name__ == '__main__':
    run()
