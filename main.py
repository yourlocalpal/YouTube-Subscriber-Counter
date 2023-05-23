import tkinter as tk
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# YouTube API credentials (replace with your own)
API_KEY = "REPLACE API KEY"

# YouTube channel ID
CHANNEL_ID = "REPLACE CHANNEL ID"

# Create YouTube API client
youtube = build("youtube", "v3", developerKey=API_KEY)


# Function to get subscriber count
def get_subscriber_count():
    try:
        # Call the YouTube API to get channel statistics
        response = youtube.channels().list(
            part="statistics",
            id=CHANNEL_ID
        ).execute()

        # Get the subscriber count from the response
        subscriber_count = int(response["items"][0]["statistics"]["subscriberCount"])

        # Update the label text with the subscriber count
        label.config(text=f"Subscriber Count: {subscriber_count}")

    except HttpError as e:
        # Display an error message if API call fails
        label.config(text="Error retrieving subscriber count")


# Create a window
window = tk.Tk()
window.title("YouTube Subscriber Count")
window.configure(bg="black")

# Create a label to display the subscriber count
label = tk.Label(window, text="Subscriber Count: ", font=("Arial", 20), fg="white", bg="black")
label.pack(pady=50)

# Call the function to get the initial subscriber count
get_subscriber_count()

# Update the subscriber count every 30 seconds (adjust as needed)
window.after(30000, get_subscriber_count)

# Run the window's main event loop
window.mainloop()
