import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import config

# Initialize OAuth2 client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    config.OAUTH2_FILE,
    ["https://www.googleapis.com/auth/youtube.force-ssl"]
)
credentials = flow.run_local_server(port=0)
youtube = googleapiclient.discovery.build(
    "youtube", "v3", credentials=credentials)

# Input YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Extract video ID from URL
if "watch?v=" in video_url:
    video_id = video_url.split("watch?v=")[1]
    if '&' in video_id:
        video_id = video_id.split('&')[0]
elif "youtu.be/" in video_url:
    video_id = video_url.split("youtu.be/")[1]
    if '&' in video_id:
        video_id = video_id.split('&')[0]
else:
    print("Invalid YouTube URL")
    exit(1)

# Input minimum number of subscribers
min_subscribers = int(input("Enter the minimum number of subscribers: "))

# Get comments from the video
request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=100,  # adjust as necessary
)
response = request.execute()

# Filter comments by channels with at least the specified number of subscribers
channels = []
for item in response["items"]:
    channel_id = item["snippet"]["topLevelComment"]["snippet"]["authorChannelId"]["value"]
    channel_request = youtube.channels().list(
        part="statistics",
        id=channel_id
    )
    channel_response = channel_request.execute()
    subscriber_count = int(channel_response["items"][0]["statistics"]["subscriberCount"])
    if subscriber_count >= min_subscribers:
        channels.append({
            "name": item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
            "link": "https://www.youtube.com/channel/" + channel_id
        })

# Output list of channels to a .txt file
with open('output.txt', 'w') as f:
    for channel in channels:
        f.write(f'Channel: {channel["name"]}, Link: {channel["link"]}\n')
