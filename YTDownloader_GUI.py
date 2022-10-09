# -*- coding: utf-8 -*-
"""
@author Jim Christop

"""

from ast import Import
from importlib.resources import path
from os import link
from tkinter import *
import tkinter.font as tkFont
from tkinter.ttk import Style
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os
from pytube import YouTube
import threading

pathToSave = "" 

def getFolderPath(): #asking user which folder he wishes to use for downloading the mp3s
   folder = filedialog.askdirectory()
   global pathToSave 
   pathToSave = str(folder) #saving the path to our global variable
   pathtxt = Label(root, height = 1, width = 55, text=folder, font=("Arial", 14) ).place(x = 5, y = 120)

def downloadMP3():
    global pathToSave #referencing our global variable
    link = entry.get() #getting the youtube link to download
    if(pathToSave != "" and link != ""): #checking if link and path are given if not, warning message will appear
        try : #using exceptions because of some abnormalities
            ######################### START DOWNLOAD AND SAVE #############################################
            youtube = YouTube(str(link)) 
            video = youtube.streams.filter(only_audio=True).first()
            out_file = video.download(output_path=pathToSave)
            naming, ext = os.path.splitext(out_file)
            new_file = naming + '.mp3'
            os.rename(out_file, new_file)
            oklbl = Label(root, text="Successfully Downloaded!", font=("Helvetica", "13"))
            oklbl.place(relx= .7, rely= .8, anchor= E)
            root.after(3000, oklbl.destroy)
            root.after(1, entry.delete(0, 'end'))
            ######################### END DOWNLOAD AND SAVE ##############################################
        except :
            #if it already exists, remove mp4
            os.remove(out_file)
            oklbl = Label(root, text="Something went wrong. Try again!\nSong might already be downloaded.", font=("Helvetica", "13"))
            oklbl.place(relx= .7, rely= .8, anchor= E)
            root.after(3000, oklbl.destroy)
            root.after(1, entry.delete(0, 'end'))    
    elif(pathToSave == "" and link == ""):
        messagebox.showwarning("Warning","Please select a folder to save MP3s\nPlease insert a link!")
    elif(pathToSave == "" and link != ""):
        messagebox.showwarning("Warning","Please select a folder to save MP3s")
    else :
        messagebox.showwarning("Warning","Please insert a link!")        

root = Tk() #creating the window
root.title("YoutubeDownlader To MP3") #setting the title 
iconphoto = PhotoImage(file="YTtoMP3_logo_transparent.png") #reading in the photo
root.iconphoto(False, iconphoto) #setting window iconphoto

width = 600 # Width of the app
height = 300 # Height of the app
screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight() # Height of the screen
x = (screen_width/2) - (width/2) #calculation to center the app
y = (screen_height/2) - (height/2)

root.resizable(0,0) #making the window unresizeable
root.geometry('%dx%d+%d+%d' % (width, height, x, y)) #setting the app in the center of the screen

lblFont = tkFont.Font(family="Helvetica", size=20, weight="bold") #font for labels
btnFont = tkFont.Font(family="Helvetica", size=14) #font for buttons

pathlbl = Label(root, text = "Select Path to Save Files :", font=lblFont ).place(relx= .3, rely= .1, anchor= CENTER) #Informational label
pathbtn = Button(root, text = "Select", font=btnFont, command=getFolderPath).place(relx= .7, rely= .1, anchor= CENTER) #utton for download folder

selectedpathlbl = Label(root, text = "Selected Path :", font=lblFont ).place(relx= .2, rely= .3, anchor= CENTER) #label for diplaying selected folder

entry = Entry(root, width= 55) #entry -> link to be downloaded
entry.place(relx= .6, rely= .6, anchor= E, height=33)

downloadbtn = Button(root, text= "Download MP3", command = downloadMP3, font=btnFont).place(relx= .74, rely= .6, anchor= CENTER) #download button

root.mainloop() #initiate mainloop a.k.a gui