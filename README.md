# Playlist Converter: YouTube to Spotify

The **Playlist Converter** is a Python script that allows you to convert a YouTube playlist into a Spotify playlist. It fetches the audio from the YouTube playlist, searches for the corresponding tracks on Spotify, and creates a new public Spotify playlist with the matched tracks.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `spotipy`
  - `pytube`

## Installation

1. Clone this repository or download the script file to your local machine.
2. Install the required Python packages using the following command:

```bash
pip install spotipy pytube
```

1. Obtain Spotify and YouTube API keys:

Create a Spotify developer account and obtain your client_id and client_secret.
Create a YouTube API key to use with the pytube library.

2. Create a keys.py file in the same directory as the script and define the following variables:

```python
# keys.py

# Spotify API keys
client_id = 'your_spotify_client_id'
client_secret = 'your_spotify_client_secret'
redirect_uri = 'http://localhost:8080'  # Replace with your redirect URI

# YouTube API key
youtube_api_key = 'your_youtube_api_key'

```

## Usage
1. Run the script using the following command:

```shell 
python playlist_converter.py
```
1. Follow the on-screen prompts:
- Enter the URL of the YouTube playlist you want to convert.
- The script will fetch the audio from the YouTube playlist and search for corresponding tracks on Spotify.
- You'll be prompted to enter the name of your new Spotify playlist.
- After the conversion is complete, the script will inform you that the playlist has been created on your Spotify account.
- Please note that due to rate limits and other restrictions of both the Spotify and YouTube APIs, there may be limitations on the number of requests you can make within a certain time frame.

## Disclaimer
This script is provided as-is and may be subject to changes in the APIs it relies on. Use it responsibly and make sure to comply with the terms of service of both Spotify and YouTube.

## Author
Suyog Prasai

## License
This project is licensed under the MIT License - see the LICENSE file for details.

