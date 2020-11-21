from tkinter import *
from tkinter import filedialog, messagebox
from pygame import mixer
import os
from os import sys
mixer.init()
x = "700"
y = "100"
root = Tk()
root.geometry(x+"x"+y)
root.title("F_player Ver.:1.4")
root.resizable(0,0)
currentFile = False
Play=False
DirFiles=""
StopState="Stop"
var=DoubleVar()
Nlista=0
music=0
music1=0
openWindow=0
lista=list(range(0))
lista2=list(range(0))
veces=list(range(0))
vlista3=""
vlista4=""
vlista5=0
V1=2
From_openWindow=True
directorio = 0
def aboutShow():
    messagebox.showinfo(title="About F_Player", message = "F_player is a free music player for mp3 and wav developed by Fernando Jelvez, version:1.4")
def aboutContact():
    messagebox.showinfo(title="Contact", message = "On GitHub:Fernando-Jelvez/Gmail:fernandojelvez2017@gmail.com")
def openFile():
    global openWindow
    global currentFile
    global V1
    global vlista5
    global vlista3
    global directorio
    global DirFiles
    vlista5=0
    openWindow = filedialog.askopenfilename(title="Open a file",initialdir="/Music", filetypes=(("Audio File","*.mp3;*.wav"),("All files","*.*")))
    currentFile=openWindow
    lista2=openWindow.split("/")
    for x in lista2:
        if not V1 == len(lista2)+1:
            veces.append(lista2[len(lista2)-V1])
            V1=V1+1
    veces.reverse()
    for x in veces:
        directorio=vlista3+veces[vlista5]+"/"
        vlista3=directorio
        vlista5=vlista5+1
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(".mp3"):
                 DirFiles=os.path.join(root, file)
                 lista.append(DirFiles)
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(".wav"):
                 DirFiles=os.path.join(root, file)
                 lista.append(DirFiles)
    music=lista.index(openWindow)
    print(DirFiles)
    playing.config(text=openWindow)
menubar = Menu(root)
files = Menu(menubar, tearoff = False)
about = Menu(menubar, tearoff = False)
contact = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "Files", menu = files)
menubar.add_cascade(label = "About F_Player", menu = about)
menubar.add_cascade(label = "Contact the developer of this app", menu = contact)
files.add_command(label = "Open file", command = openFile)
about.add_command(label = "About", command = aboutShow)
contact.add_command(label = "Contact", command = aboutContact)
root.config(menu=menubar)
def sel(x):
    global selection
    selection = (var.get()/100)
    mixer.music.set_volume(selection)
def Music():
    global texto4
    newtext.config(text=texto4)
    botonNuevo7.place_forget()
    botonNuevo8.place_forget()
    botonNuevo9.place_forget()
    botonNuevo10.place_forget()
    botonPlay.place(x=375,y=250)
    botonStop.place(x=475,y=250)
    botonPrevious.place(x=575,y=250)
    botonNext.place(x=675,y=250)
    mixer.music.pause()
def Play():
    global Play
    Play=True
    try:
        if From_openWindow == True:
            if StopState=="Stop":
                mixer.music.load(currentFile)
                mixer.music.play()
            if StopState=="Pause":
                mixer.music.unpause()
        if From_openWindow == False:
            if StopState=="Stop":
                mixer.music.load(lista[music])
                mixer.music.play()
            if StopState=="Pause":
                mixer.music.unpause()
    except TypeError:
        messagebox.showinfo(title="Error", message = "You must choose a valid file")
def Stop():
    mixer.music.pause()
    global Play
    Play=False
    global StopState
    StopState="Stop"
def Pause():
    mixer.music.pause()
    global Play
    Play=False
    global StopState
    StopState="Pause"
def Next():
    global From_openWindow
    global music
    From_openWindow=False
    if not music==len(lista):
        music1=music+1
        music=music1
        Prev_Next()
def Previous():
    global From_openWindow
    global music
    From_openWindow=False
    music1=music-1
    music=music1
    Prev_Next()
def Prev_Next():
    if Play == True:
        try:
            mixer.music.load(lista[music])
            mixer.music.play()
        except:
            messagebox.showinfo(title="Error", message = "File not supported")
    playing.config(text=lista[music])

w = Scale(root, from_=0, to=100, orient=HORIZONTAL,variable=var,command=sel)
w.place(x=550,y=25)
w.set(100)
botonPlay= Button(root,text="4",font=("Webdings",15),compound="top",command=Play)
botonPlay.place(x=200,y=25)

botonStop= Button(root,text="g",font=("Webdings",15),compound="top",command=Stop)
botonStop.place(x=250,y=25)

botonPause= Button(root,text=";",font=("Webdings",15),compound="top",command=Pause)
botonPause.place(x=150,y=25)

botonPrevious= Button(root,text="9",font=("Webdings",12),compound="top",command=Previous,pady=1,padx=6)
botonPrevious.place(x=100,y=25)

botonNext= Button(root,text=":",font=("Webdings",12),compound="top",command=Next,pady=1,padx=6)
botonNext.place(x=300,y=25)

playing=Label(root,text="No file",font=("Calibri",10,))
playing.place(x=100,y=5)

root.mainloop()

