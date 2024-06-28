"""subpackage module."""

from __future__ import annotations

import requests
from youtube_transcript_api import YouTubeTranscriptApi

API_KEY = "AIzaSyA9HJCS9aqopIa54BI1N_R3KDpAGk6F3oQ"
CHANNEL_NAME = "글로벌공대인"


def get_channel_id(channel_name: str, youtube_api_key: str) -> str:
    """Get the channel ID for a given channel name."""
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&q={channel_name}&key={youtube_api_key}"
    response = requests.get(search_url, timeout=10).json()
    return response["items"][0]["id"]["channelId"]


def get_list_of_videos(
    channel_name: str, youtube_api_key: str, channel_id: str | None = None
) -> list:
    """Get a list of video IDs for a given channel ID."""
    video_ids = []
    next_page_token = None
    if not channel_id:
        channel_id = get_channel_id(channel_name, youtube_api_key)

    while True:
        upload_url = f"https://www.googleapis.com/youtube/v3/search?key={youtube_api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=50"
        if next_page_token:
            upload_url += f"&pageToken={next_page_token}"
        response = requests.get(upload_url, timeout=10).json()

        for item in response["items"]:
            if item["id"]["kind"] == "youtube#video":
                video_ids.append(item["id"]["videoId"])

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break
    return video_ids


def download_youtube_transcript(
    video_ids: list, language_code: str = "kr"
) -> None:
    """Download the transcript of a YouTube video in a specific language."""
    for video_id in video_ids:
        try:
            # Fetch the transcript in the specified language
            transcript = YouTubeTranscriptApi.get_transcript(
                video_id, languages=[language_code]
            )

            # Combine the transcript text into a single string
            transcript_text = "\n".join([item["text"] for item in transcript])

            # Save the transcript to a file
            with open(
                f"{video_id}_transcript_{language_code}.txt",
                "w",
                encoding="utf-8",
            ) as file:
                file.write(transcript_text)

            print(
                f"Transcript downloaded and saved as {video_id}_transcript_{language_code}.txt"
            )

        except Exception as e:
            print(f"An error occurred: {e}")
