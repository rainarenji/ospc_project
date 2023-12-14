import googleapiclient.discovery
from googleapiclient.errors import HttpError

import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv('api_key')


# Create a YouTube API client
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

def get_video_comments(video_id):
    try:
        # Get comments for the specified video
        results = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText"
        ).execute()

        # Extract and print comments
        for item in results["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            print(comment)

    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred: {e.content}")

# Specify the video ID for the desired YouTube video
video_id = "VnePyGPDtP4"

# Get and print comments
get_video_comments(video_id)
