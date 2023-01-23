from pytube import YouTube
import os

# Prompt user for file containing YouTube links
file_path = input("Enter the path of the file containing the YouTube links: ")

# Open the file and read the links
with open(file_path, 'r') as file:
    links = file.readlines()

# Iterate through the links and download each video
for link in links:
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    # Download the video to the current working directory
    out_file = video.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " has been successfully downloaded.")
