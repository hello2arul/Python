from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from constants import my_client_id, my_client_secret

date = input("What year would you like to travel to ?(YYYY-MM-DAY): ")
URL = f"https://www.billboard.com/charts/hot-100/{date}" 

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=f"https://developer.spotify.com/dashboard/applications/{my_client_id}",
        client_id=my_client_id,
        client_secret=my_client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]


#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)
#Adding songs found into the new playlist
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)
