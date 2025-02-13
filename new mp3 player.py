# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 06:17:53 2023

@author: BEST SOLUTION
"""


from tkinter import *
from pygame import mixer
import os
from tkinter import filedialog

mixer.init()

m1=Tk()
m1.geometry("800x400")



def browse():
    
    file=filedialog.askopenfilename(initialdir="D:\music")
    s=file.split("/")[-1]
    playlist.insert(END,s)
    

def resume():
    mixer.music.unpause()
    
    
def pause():
    mixer.music.pause()

def play():
    current=playlist.get(ACTIVE)
    mixer.music.load(current)
    mixer.music.play()
    
def stop():
    mixer.music.stop()

def refresh():
    playlist.delete(0,END)
    os.chdir=os.chdir(r"D:\music")
    songs=os.listdir()
    for s in songs:
        playlist.insert(END,s)
            
       



f1=Frame(m1,width=800,height=200,bg="#808080")
f1.pack(side=TOP)
f2=Frame(m1,width=800,height=200,bg="blue")
f2.pack(side=TOP)

l1=Label(m1,text="MP3 PLAYER",fg="orange",bg="#808080",font="Helvatica 40")
l1.place(x=250,y=50)





b1=Button(m1,text="Browse",fg="yellow",bg="black",command=browse)
b1.place(x=290,y=350)
b2=Button(m1,text="Resume",command=resume,bg="orange")
b2.place(x=110,y=250)

b3=Button(m1,text="Pause a song",command=pause,bg="yellow")
b3.place(x=50,y=300)

b4=Button(m1,text="Play a song",command=play,bg="green")
b4.place(x=160,y=300)

b5=Button(m1,text="Stop a song",command=stop,bg="red")
b5.place(x=100,y=350)


b6=Button(m1,text="Refresh",command=refresh,bg="yellow")
b6.place(x=600,y=350)



playlist=Listbox(m1,selectmode=SINGLE)
playlist.place(x=400,y=200)
























m1.mainloop()