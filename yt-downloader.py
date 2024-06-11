from pytube import YouTube
import os
import sys  

link = sys.argv[1]

yt = YouTube(link)

print("Title: ", yt.title)
print("Length of video: ", yt.length, "seconds")

input("Press Enter to continue...")

ys = yt.streams.get_highest_resolution()
# yd = yt.streams.get_by_resolution("1080p")

yd = ys.download('/home/voga/Downloads')