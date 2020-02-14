'''
A simple python based gui application to download videos from youtube.
- By B.Shubankar
'''

import tkinter as tk
import os
import youtube_dl
from tkinter import *
from tkinter.ttk import *

def get_video_url():
   search_item = download_entry.get()
   ydl_opts = {
      'format': 'best',
      'noplaylist': True,
      'extract-audio': True,
   }
   os.chdir('C:/Users/rohit/Desktop/download')
   with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([search_item])

root = tk.Tk()
pic = PhotoImage(file ='C://Users//rohit//Documents//GitHub//GUI-Video-Downloader//index.jpg')
root.iconphoto(False,pic)
root.title('Video Downloader')
canvas1 = tk.Canvas(root,height = 400, width=400, bg="#263d42")
canvas1.pack()
download_entry = tk.Entry(root)
canvas1.create_window(200,140,window=download_entry)
download = tk.Button(text= "Download", padx=5,pady=5,fg = "white",bg = "DeepSkyBlue4",command = get_video_url)
canvas1.create_window(200,230,window=download)
root.mainloop()
