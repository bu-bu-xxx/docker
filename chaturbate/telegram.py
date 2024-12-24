from pyrogram import Client

YOUR_API_ID = 

# Replace 'my_bot' with your bot's name, 'API_ID', and 'API_HASH' with your credentials
app = Client("my_bot", api_id=YOUR_API_ID, api_hash="YOUR_API_HASH")

video_file_path = "path/to/your/video.mp4"  # Change this to the path of your video file
group_id = -1001234567890  # Change this to your group's ID (can be negative for groups)

with app:
    app.send_video(chat_id=group_id, video=video_file_path)

print("Video uploaded successfully.")