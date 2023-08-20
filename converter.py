import spotify
from keys import *
from pytube import Playlist
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

class Converter: 

    def __init__(self) -> None: 
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
    
        self.yt_playlist_url = None
        self.sp_initialization = self.sp_init()

    def get_songs_yt(self) -> list:
        plist = Playlist(self.yt_playlist_url)
        playlist_title = plist.title
        videos = plist.videos
        titles = []
        print("[SONGS IN THE PLAYLIST]")
        for index, video in enumerate(videos, 1): 
            titles.append(video.title)
            print(f"({index}). [{video.title}]")
        

        try: 
            plist = Playlist(self.yt_playlist_url)
            playlist_title = plist.title
            videos = plist.videos
            titles = []
            for video in videos: 
                titles.append(video.title)

            return titles

        except Exception as e: 
            print("[ERROR] Failed to initialize the playlist", e)

    def sp_init(self) -> object: 
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope="playlist-modify-public"
        ))

        return sp

    def sp_get_song(self, query, sp=None) -> str:
        sp = self.sp_initialization
        search_results = sp.search(q=query, type='track', limit='10')
        uris = []
        for track in search_results['tracks']['items']: 
            uris.append(track['uri'])
        track_main = uris[0]

        return track_main

    def sp_get_playlist(self, songs, sp=None) -> list:
        sp = self.sp_initialization        
        sp_uris = []
        for song in songs:
            uri = self.sp_get_song(song)
            sp_uris.append(uri)
        return sp_uris

    def sp_create_playlist(self, uris, sp=None) -> int:
        sp = self.sp_initialization
        playlist_name = input("Enter the name of your playlist: ")

        user_id = sp.me()['id'] # Get the users id
        playlist = sp.user_playlist_create(user_id, playlist_name, public=True)
        sp.user_playlist_add_tracks(user_id, playlist['id'], uris)
        

def main() -> int: 
    ci = Converter()

    url = input("Enter the url of the playlist: ")
    ci.yt_playlist_url = url
    try:
        songs = ci.get_songs_yt()
        print("[INFO] Successfully fetched Audio from the youtube playlist")
    except Exception as e: 
        print("[ERROR] Failed to fetch songs from youtube", e)
    try:
        sp_songs_uris = ci.sp_get_playlist(songs)
        print("[INFO] Succesfully scanned uris through spotify api")
    except Exception as e:
        print("[ERROR] Failed to fetch songs from spotify", e)
    try:
        ci.sp_create_playlist(sp_songs_uris)
        print("[INFO] Successfully created the playlist")
        print("[INFO] Check your spotify account")
    except Exception as e: 
        print("[ERROR] Failed to add playlist to spotify", e)

    return 0

if __name__ == "__main__": 
    main()