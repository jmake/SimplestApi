import os 
import time
import subprocess

from pytubefix import YouTube
from pytubefix.cli import on_progress

def list_directory(path="."):
    try:
        for entry in os.listdir(path):
            print(entry)
    except PermissionError:
        print(f"Permission denied: {path}")

def download_video_segment(video_id):
  url = f"https://www.youtube.com/watch?v={video_id}"
  #print( url )
  print(f"download_video_segment:'{url}'")
  
  yt = YouTube(url, on_progress_callback = on_progress, use_po_token=True)
  #print(f"title:'{yt.title}'")

  ys = yt.streams.get_highest_resolution()
  ys.download(filename="temp_video.mp4")
  
  list_directory( os.getcwd() )
  

if __name__ == "__main__" :
    video_id="paxrBTnda78"
    download_video_segment(video_id) 

