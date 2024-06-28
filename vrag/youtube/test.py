from vrag.youtube.common.utility import (
    download_youtube_transcript,
    get_list_of_videos,
)

video_ids = get_list_of_videos(
    "글로벌공대인", "AIzaSyA9HJCS9aqopIa54BI1N_R3KDpAGk6F3oQ"
)
download_youtube_transcript(video_ids, "ko")
