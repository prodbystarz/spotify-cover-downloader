# spotify-cover-downloader

this script allows you to download and resize spotify cover images for tracks or albums. it is compatible with both windows and mac.

## features
- download spotify cover images for tracks and albums
- resize images to 3000x3000 pixels
- save images to your downloads folder

## requirements
- python 3.x
- spotipy
- requests
- pillow
- certifi (optional but my computer needed it for some reason)

## installation
1. clone the repository:
    ```sh
    git clone https://github.com/prodbystarz/spotify-cover-downloader.git
    cd spotify-cover-downloader
    ```

2. install the required packages:
    ```sh
    pip3 install spotipy requests pillow certifi
    ```

3. set your spotify api credentials in the script:
    ```python
    SPOTIPY_CLIENT_ID = 'your_spotify_client_id'
    SPOTIPY_CLIENT_SECRET = 'your_spotify_client_secret'
    ```

## usage
1. run the script:
    ```sh
    python app.py
    ```

2. enter the spotify track or album url when prompted.

## compatibility
- windows
- mac

## license
this project is licensed under the mit license.
