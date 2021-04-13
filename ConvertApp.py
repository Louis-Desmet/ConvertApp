#install required library (moviepy)
import os
os.system("pip install moviepy")
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo


def MakeVideo(VidName,fps):
    try:
        mp4 = VideoFileClip(VidName)
        mp4.write_gif("mygif.gif",fps)
        showinfo(title="Succes", message="Video was succesfully converted to 'mygif.gif'")
        
    except OSError:
        print("video does not exist")
        showerror(title = "Error", message = "video does not exist or was not placed in the folder")

    except ZeroDivisionError:
        print("fps to low")
        showerror(title = "Error", message = "fps to low")


def getvalueAndMake():
    NameVid = VidName.get()
    Thefps = fps.get()             
    MakeVideo(NameVid,Thefps)



#GUI
from tkinter import *
from moviepy.editor import VideoFileClip
from tkinter import ttk

window = Tk()
window.title("Convert MP4 to Gif")
window.geometry("300x200")

#label
l1 = Label(window, text = "CONVERT MP4 TO GIF")
l1.grid(row = 0,column = 0)

l2 = Label(window, text="Video title: ")
l2.grid(row = 2,column = 0)

l3 = Label(window, text="Amount of fps: ")
l3.grid(row = 3,column = 0)



#inputs
VidName = StringVar()
e1 = Entry(window,textvariable = VidName)
e1.grid(row = 2,column = 1)


fps = IntVar()
e2 = Entry(window,textvariable = fps)
e2.grid(row = 3,column = 1)

#button
b1 = ttk.Button(window,text = "Make Gif")
b1.config(command = getvalueAndMake)
b1.grid(row = 5,column = 0)

window.mainloop()



