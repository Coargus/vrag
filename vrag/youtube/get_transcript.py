from youtube_transcript_api import YouTubeTranscriptApi


def download_youtube_transcript(video_id, language_code="ko") -> None:
    """Download the transcript of a YouTube video in a specific language."""
    try:
        # Fetch the transcript in the specified language
        transcript = YouTubeTranscriptApi.get_transcript(
            video_id, languages=[language_code]
        )

        # Combine the transcript text into a single string
        transcript_text = "\n".join([item["text"] for item in transcript])

        # Save the transcript to a file
        with open(
            f"{video_id}_transcript_{language_code}.txt", "w", encoding="utf-8"
        ) as file:
            file.write(transcript_text)

        print(
            f"Transcript downloaded and saved as {video_id}_transcript_{language_code}.txt"
        )

    except Exception as e:
        print(f"An error occurred: {e}")


# Replace 'YOUR_VIDEO_ID' with the actual YouTube video ID
id = [
    "hHeDOGQxrn4",
    "k4F9Mcg9wKs",
    "z6SB8w3FncM",
    "IMTCsuczU68",
    "jBLfZV4NC2U",
    "JS67Oweu-pE",
    "sFLZK548-Ro",
    "2PMxlZkLaHo",
    "nNdF184fKiA",
    "qydIP_BO_Og",
    "5yWPkQkG4SM",
    "hIKL7bAyskk",
]
for i in id:
    download_youtube_transcript(i, "ko")
# download_youtube_transcript("k4F9Mcg9wKs", "ko")
