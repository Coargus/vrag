"""subpackage module."""

import requests

API_KEY = "AIzaSyA9HJCS9aqopIa54BI1N_R3KDpAGk6F3oQ"
CHANNEL_NAME = "글로벌공대인"


def get_channel_id(channel_name):
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&q={channel_name}&key={API_KEY}"
    response = requests.get(search_url).json()
    channel_id = response["items"][0]["id"]["channelId"]
    return channel_id


# Get Channel ID
search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&q={CHANNEL_NAME}&key={API_KEY}"
response = requests.get(search_url).json()
channel_id = response["items"][0]["id"]["channelId"]

# Get all video IDs
video_ids = []
next_page_token = None

while True:
    upload_url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=50"
    if next_page_token:
        upload_url += f"&pageToken={next_page_token}"
    response = requests.get(upload_url).json()

    for item in response["items"]:
        if item["id"]["kind"] == "youtube#video":
            video_ids.append(item["id"]["videoId"])

    next_page_token = response.get("nextPageToken")
    if not next_page_token:
        break

print(video_ids)
