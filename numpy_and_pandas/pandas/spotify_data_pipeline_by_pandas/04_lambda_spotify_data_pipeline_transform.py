import json
import boto3
from datetime import datetime
from io import StringIO
import pandas as pd


def lambda_handler(event, context):
    s3 = boto3.client("s3")
    Bucket = "spotify-data-pipeline-heidi"
    Key = "raw_data/to_processed/"

    # Information about the files present in bucket is returned as dictionary
    files_in_bucket_dict = s3.list_objects(Bucket=Bucket, Prefix=Key)

    # We are not interetsed in all non-sence data.
    # There will be a key named "contents" which is list.
    # That list contains information about files.

    file_keys = []
    for file in files_in_bucket_dict["Contents"]:
        # One of the file contains details about just the folder in wchih these files are stored.
        # and we are not interested in it. We are interested only on json files.
        for file in s3.list_objects(Bucket=Bucket, Prefix=Key)["Contents"]:
            file_key = file["Key"]
            if file_key.split(".")[-1] == "json":
                response = s3.get_object(Bucket=Bucket, Key=file_key)
                content = response["Body"]
                jsonObject = json.loads(content.read())
                data = jsonObject
                file_keys.append(file_key)

    # Take only the elements which you are interested in
    songs_list = []
    for row in data["items"]:
        song_id = row["track"]["id"]
        song_name = row["track"]["name"]
        song_duration = row["track"]["duration_ms"]
        song_url = row["track"]["external_urls"]["spotify"]
        song_popularity = row["track"]["popularity"]
        song_added = row["added_at"]
        album_id = row["track"]["album"]["id"]
        artist_id = row["track"]["album"]["artists"][0]["id"]
        song_element = {
            "song_id": song_id,
            "song_name": song_name,
            "duration_ms": song_duration,
            "url": song_url,
            "popularity": song_popularity,
            "song_added": song_added,
            "album_id": album_id,
            "artist_id": artist_id,
        }
        songs_list.append(song_element)

    # Converting songs dictionary
    songs_df = pd.DataFrame.from_dict(songs_list)

    # Data transformation
    songs_df["song_added"] = pd.to_datetime(songs_df["song_added"])

    # Storing the transformed data into s3 bucket
    songs_key = "transformed_data/" + str(datetime.now()) + ".csv"
    songs_buffer = StringIO()
    songs_df.to_csv(songs_buffer, index=False)
    songs_content = songs_buffer.getvalue()
    s3.put_object(Bucket=Bucket, Key=songs_key, Body=songs_content)

    # Once transformation is completed, move the file from "to_transformed" to "transformed"
    s3_resource = boto3.resource("s3")
    for key in file_keys:
        copy_source = {"Bucket": Bucket, "Key": key}
        s3_resource.meta.client.copy(
            copy_source, Bucket, "raw_data/processed/" + key.split("/")[-1]
        )
        # s3_resource.delete_object(Bucket, Key)
