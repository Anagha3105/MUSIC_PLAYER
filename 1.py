# first installing mutagen, pygame--->modules
import os
import pygame
import tkinter
import random
from tkinter.filedialog import askdirectory

root = tkinter.Tk()
root.minsize(450, 450)
root.title('Music Player')

songs = []  # to store all the songs
titles = []
s = 0
message = 'Now playing : '

'''def shuffle_playlist():
    global songs
    songs = random.shuffle(songs)
    listbox.delete(0, listbox.size())
    for i in range(len(songs) - 1, -1, -1):
        listbox.insert(0, songs[i])'''
#def loop:
#def delete_song:
#jump
#pause

def next_song(event):
    global s
    s += 1
    pygame.mixer.music.load(songs[s])
    pygame.mixer.music.play()
    updatelabel()


def prev_song(event):
    global s
    s -= 1
    pygame.mixer.music.load(songs[s])
    pygame.mixer.music.play()
    updatelabel()


def stop_song(event):
    pygame.mixer.music.stop()
    v.set(message)
    return song_label


def updatelabel():
    global s
    v.set(message + songs[s])


def directorychooser():
    directory = askdirectory()
    os.chdir(directory)
    
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            songs.append(files)
            print(files)

    pygame.mixer.init()  # initialising
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()


directorychooser()

label = tkinter.Label(root, text = "Music Player")
label.place(relx = 0.45, rely = 0)

listbox = tkinter.Listbox(root, height = 25, width = 60, fg = 'white', bg = 'dark magenta')
listbox.place(relx = 0.35, rely = 0.05)

v = tkinter.StringVar()
v.set(message + songs[s])
song_label = tkinter.Label(root, textvariable = v, width = 65)
song_label.place(relx = 0.30, rely = 0.67)

for i in range(len(songs) - 1, -1, -1):
    listbox.insert(0, songs[i])

next_button = tkinter.Button(root, text = "Next", width = 12, height = 3, fg = 'black', bg = 'turquoise')
next_button.place(relx = 0.7, rely = 0.3)

prev_button = tkinter.Button(root, text = "Previous", width = 12, height = 3, fg = 'black', bg = 'turquoise')
prev_button.place(relx = 0.2, rely = 0.3)

stop_button = tkinter.Button(root, text = "Stop", width = 12, height = 3, fg = 'black', bg = 'turquoise')
stop_button.place(relx = 0.35, rely = 0.72)

#shuffle_button = tkinter.Button(root, text = 'Shuffle Playlist',command = shuffle_playlist, width = 12, height = 3, fg = 'black', bg = 'turquoise')
#shuffle_button.place(relx = 0.55, rely = 0.72)

next_button.bind(" <Button-1> ", next_song)
prev_button.bind(" <Button-1> ", prev_song)
stop_button.bind(" <Button-1> ", stop_song)

root.mainloop() 