import pygame
import tkinter as tk
from tkinter import filedialog
import os

player = tk.Tk()
player.title("Music Player")
player.geometry("310x325")

song_title = tk.StringVar()
song_title.set("Select the song to Play")

os.chdir(filedialog.askdirectory())
songlist = os.listdir()

playing = tk.Listbox(player, font="Helvetica 12 bold", width=28, bg="white", selectmode=tk.SINGLE)

for item in songlist:
    playing.insert(0, item)

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playing.get(tk.ACTIVE))
    name = playing.get(tk.ACTIVE)
    song_title.set(f"{name[:16]}..." if len(name) > 18 else name)
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

def stop():
    pygame.mixer.music.stop()

text = tk.Label(player, font="Helvetica", textvariable=song_title).grid(row=0, columnspan=3)
playing.grid(columnspan=3, row=1)

playB = tk.Button(player, width=7, height=1, font="Helvetica", text="Play", command=play, bg="lightgreen").grid(row=2, column=0)
pauseB = tk.Button(player, width=7, height=1, font="Helvetica", text="Pause", command=pause, bg="yellow").grid(row=2, column=1)
resumeB = tk.Button(player, width=7, height=1, font="Helvetica", text="Resume", command=resume, bg="lightgreen").grid(row=2, column=2)
stopB = tk.Button(player, width=7, height=1, font="Helvetica", text="Stop", command=stop, bg="red").grid(row=2, column=3)

player.mainloop()