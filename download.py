from pytube import YouTube
from pytube import Search
import sys
import moviepy.editor as mp
import numpy as np
import os
import glob
def Download(singer,number,duration):
    number=int(number)
    duration=int(duration)
    if not os.path.exists(f"static/{singer}"):
        os.makedirs(f"static/{singer}")
    
    SAVE_PATH = f"static/{singer}"
    query=singer + ' music videos'
    s = Search(query)
    
    i=0
    
    # for i in range(0,number):
    for v in s.results:
     if i < number and v.length < 600:
        
        try:
            youtubeObject = YouTube(v.watch_url)
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            youtubeObject.download(SAVE_PATH,filename=f"{i}.mp4")
            print(f"Downloaded {i} video")
            i=i+1
        except:
            print("An error has occurred")
        

    for k in range(0, number):
        try:
            clip = mp.VideoFileClip(f"static/{singer}/{k}.mp4").subclip(15,duration+15)
            clip.audio.write_audiofile(f"static/{singer}/{k}.mp3")
        except:
            sys.exit(0)

  

    audio_clips = [mp.AudioFileClip(f"static/{singer}/{j}.mp3") for j in range(0, number)]
    final_clip = mp.concatenate_audioclips(audio_clips)
    final_clip.write_audiofile(f"{SAVE_PATH}/mashup.mp3")

    

