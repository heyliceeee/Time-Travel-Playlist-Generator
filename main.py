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

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private", redirect_uri="http://127.0.0.1:4202", client_id=os.getenv("SPOTIFY_CLIENT_ID"), client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"), show_dialog=True, cache_path="token.txt", username=os.getenv("SPOTIPY_USERNAME"))) # Create a Spotify object
user_id = sp.current_user()["id"] # Get the ID of the current user

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
    endpoint = f"{BAKEBOARD_URL}/{date}/"
    response = requests.get(endpoint, headers=HEADERS) # Make a GET request to the API endpoint
    return response
def create_playlist():
    """
    Create a new playlist for the top songs.
    :return: playlist ID
    """
    playlist = sp.current_user_playlist_create(name=f"Top Songs for {original_date}", public=False, description="Automatically generated playlist")
    return playlist["id"]
def search_songs():
    """
    search songs in spotify
    """
    year_date = saturday_date.strftime("%Y")  # Extract the year from the Saturday date
    song_uris = []
    for song in song_names:  # for each song in the list of song names
        results = sp.search(q=f"track:{song} year:{year_date}", type="track")  # Search for the song in Spotify

        if results["tracks"]["total"] > 0:  # If the song is found in Spotify
            song_uri = results["tracks"]["items"][0]["uri"]  # Get the URI of the first matching track
            song_uris.append(song_uri)  # Add the URI to the list of song URIs
    print(f"Song URIs: {song_uris}")

while True:
    date_str = input("Which year do you want to travel to? (YYYY-MM-DD): ")

    if is_valid_date(date_str): # Check if the input is a valid date
        original_date = datetime.datetime.strptime(date_str, "%Y-%m-%d") # Convert the input date string to a datetime object
        saturday_date = next_saturday(original_date) # Get the next Saturday after the original date
        saturday_str = saturday_date.strftime("%Y-%m-%d") # Convert the Saturday date to a string in the format YYYY-MM-DD

        songs = get_top_songs(saturday_str) # Call the function to get the top songs for the given date
        soup = BeautifulSoup(songs.text, "html.parser") # Parse the HTML response
        song_names = [tag.getText().strip() for tag in soup.select("h3.chart-entry__title")] # Extract song names from the HTML

        search_songs() # search songs in spotify

        #playlist_id = create_playlist()
        #print(f"Playlist created: {playlist_id}")
        break

    print("Invalid date. Please enter a valid date in the format YYYY-MM-DD.")