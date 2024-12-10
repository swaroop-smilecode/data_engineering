import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
import json
from datetime import datetime


def lambda_handler(event, context):
    # Environment variables
    cilent_id = os.environ.get("client_id")
    client_secret = os.environ.get("client_secret")

    # Authticate & get spotify api object
    client_credentials_manager = SpotifyClientCredentials(
        client_id=cilent_id, client_secret=client_secret
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Identify the URI of playlist you need
    playlist_link = "https://open.spotify.com/playlist/2YRe7HRKNRvXdJBp9nXFza"
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]

    # Call the method named playlist_tracks by passing the URI.
    # This method will give back, list of songs in that playlist.
    raw_data = sp.playlist_tracks(playlist_URI)

    cilent = boto3.client("s3")
    filename = "spotify_raw_" + str(datetime.now()) + ".json"
    cilent.put_object(
        Bucket="spotify-data-pipeline-heidi",
        Key="raw_data/to_processed/" + filename,
        Body=json.dumps(raw_data),
    )
