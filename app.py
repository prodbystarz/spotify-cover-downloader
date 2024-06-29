import os
import requests
from PIL import Image
from io import BytesIO
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import urllib.parse
import certifi

SPOTIPY_CLIENT_ID = 'your_spotify_client_id'
SPOTIPY_CLIENT_SECRET = 'your_spotify_client_secret'

def get_spotify_cover_image_url(spotify_url):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                               client_secret=SPOTIPY_CLIENT_SECRET))
    
    parsed_url = urllib.parse.urlparse(spotify_url)
    path_parts = parsed_url.path.split('/')
    
    if len(path_parts) < 3:
        raise ValueError('Invalid Spotify URL')

    item_type = path_parts[1]
    item_id = path_parts[2]
    
    if item_type == 'track':
        item = sp.track(item_id)
        image_url = item['album']['images'][0]['url']
    elif item_type == 'album':
        item = sp.album(item_id)
        image_url = item['images'][0]['url']
    else:
        raise ValueError('URL must be for a track or an album')
    
    return image_url

def download_and_resize_image(image_url, save_path, size=(3000, 3000)):
    response = requests.get(image_url, verify=certifi.where())
    image = Image.open(BytesIO(response.content))
    image = image.resize(size, Image.LANCZOS)
    image.save(save_path)

def main():
    spotify_url = input("Enter the Spotify track or album URL: ")
    downloads_folder = os.path.expanduser('~/Downloads')
    
    try:
        image_url = get_spotify_cover_image_url(spotify_url)
        file_name = 'spotify_cover.jpg'
        save_path = os.path.join(downloads_folder, file_name)
        
        download_and_resize_image(image_url, save_path)
        print(f"Cover image downloaded and saved to {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
