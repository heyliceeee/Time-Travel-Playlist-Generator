import datetime
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

BAKEBOARD_URL = os.getenv("BAKEBOARD_URL")
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
MIN_DATE = datetime.datetime(2020, 8, 9) # Set the minimum date to August 9, 2020
MAX_DATE = datetime.datetime(2026, 4, 18) # Set the minimum date to April 18, 2026

print("🔑 Authenticating with Spotify...")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private", redirect_uri="http://127.0.0.1:4202", client_id=os.getenv("SPOTIFY_CLIENT_ID"), client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"), show_dialog=True, cache_path="token.txt", username=os.getenv("SPOTIPY_USERNAME"))) # Create a Spotify object
user_id = sp.current_user()["id"] # Get the ID of the current user
print("✔ Authenticated")

def is_valid_date(date_str, date_format="%Y-%m-%d"):
    """
    Check if the input date is valid based on the specified date format.
    :param date_str: date string
    :param date_format: date format string
    :return: true if the date string matches the specified format, false otherwise
    """
    try:
        parsed = datetime.datetime.strptime(date_str, date_format) # Parse the date string
        return MIN_DATE <= parsed <= MAX_DATE  # Check if the date is within the specified range
    except (ValueError, TypeError): # Return False if the date string is not in the expected format
        return False
def next_saturday(date_obj):
    """
    Get the next Saturday after the given date.
    :param date_obj: datetime object
    :return: the next Saturday after the given date
    """
    weekday = date_obj.weekday()  # Monday=0 ... Sunday=6
    days_until_saturday = (5 - weekday) % 7 # Calculate the number of days until Saturday
    return date_obj + datetime.timedelta(days=days_until_saturday) # Return the next Saturday
def get_top_songs(date):
    """
    Get the top songs for the given date.
    :param date: date string
    :return: top songs for the given date
    """
    print(f"🌐 Fetching Bakeboard songs for {date}...")
    endpoint = f"{BAKEBOARD_URL}/{date}/"
    response = requests.get(endpoint, headers=HEADERS) # Make a GET request to the API endpoint
    return response
def get_existing_playlist(name):
    """
    Get the ID of an existing playlist by name.
    :param name: Name of the playlist
    :return: ID of the playlist, or None if not found
    """
    print(f"🔍 Checking if playlist already exists: {name}")
    playlists = sp.current_user_playlists(limit=50) # Get the user's playlists

    for playlist in playlists["items"]: # Iterate through the playlists
        if playlist["name"] == name: # Check if the playlist name matches the given name
            print("✔ Playlist found! Reusing it.\n")
            return playlist["id"] # Return the playlist ID

    print("ℹ Playlist not found. A new one will be created.\n")
    return None # Return None if the playlist is not found
def create_or_get_playlist():
    """
    Create a new playlist for the top songs.
    :return: playlist ID
    """
    playlist_name = f"Top Songs for {original_date.date()}" # Name of the playlist

    existing = get_existing_playlist(playlist_name) # Check if the playlist already exists
    if existing: # If the playlist exists, return its ID
        return existing # Return the existing playlist ID

    print("🎧 Creating new playlist...")
    playlist = sp.current_user_playlist_create(name=playlist_name, public=False, description="Automatically generated playlist") # Create a new playlist
    print(f"✔ Playlist created: {playlist_name}\n")
    return playlist["id"] # Return the ID of the newly created playlist
def search_songs():
    """
    search songs in a spotify
    :return: list of song URIs
    """
    print("🎵 Searching for songs on Spotify...")
    year_date = saturday_date.strftime("%Y")  # Extract the year from the Saturday date
    song_uris = []
    for song in song_names:  # for each song in the list of song names
        print(f"   🔎 Searching: {song} ({year_date})")
        results = sp.search(q=f"track:{song} year:{year_date}", type="track")  # Search for the song in Spotify

        if results["tracks"]["total"] > 0:  # If the song is found in Spotify
            song_uri = results["tracks"]["items"][0]["uri"]  # Get the URI of the first matching track
            song_uris.append(song_uri)  # Add the URI to the list of song URIs
    print(f"\n✔ Total songs found on Spotify: {len(song_uris)}\n")
    return song_uris # return the list of song URIs
def add_songs_playlist(id, songs_list):
    """
    Add songs to the playlist.
    :param id: playlist ID
    :param songs_list: songs list
    """
    print(f"➕ Adding {len(songs_list)} songs to the playlist...")
    sp.playlist_add_items(playlist_id=id, items=songs_list) # Add songs to the playlist
    print("✔ Songs added successfully!\n")

while True:
    date_str = input("Which year do you want to travel to? (YYYY-MM-DD): ")

    if is_valid_date(date_str): # Check if the input is a valid date
        print("\n📅 Valid date. Processing...\n")
        original_date = datetime.datetime.strptime(date_str, "%Y-%m-%d") # Convert the input date string to a datetime object
        saturday_date = next_saturday(original_date) # Get the next Saturday after the original date
        saturday_str = saturday_date.strftime("%Y-%m-%d") # Convert the Saturday date to a string in the format YYYY-MM-DD

        songs = get_top_songs(saturday_str) # Call the function to get the top songs for the given date
        soup = BeautifulSoup(songs.text, "html.parser") # Parse the HTML response
        song_names = [tag.getText().strip() for tag in soup.select("h3.chart-entry__title")] # Extract song names from the HTML

        songs_uri = search_songs() # search songs in spotify
        playlist_id = create_or_get_playlist() # Create a new playlist or get the existing playlist
        add_songs_playlist(playlist_id, songs_uri) # Add songs to the playlist
        print("🎉 Process completed!")
        break

    print("Invalid date. Please enter a valid date in the format YYYY-MM-DD.")