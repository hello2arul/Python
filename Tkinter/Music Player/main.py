from tkinter import *
import pygame

window = Tk()
window.title("Mp3 player")
window.geometry("500x300")

# for sound
pygame.mixer.init()

def previous_song():
    pass

def next_song():
    pass

def play():
    pass

def pause():
    pass

def stop():
    pass


frame = Frame(window)
frame.pack(pady=20)

playlist_box = Listbox(window, bg="black", fg="green", width=60)
playlist_box.grid(row=0, column=0)


# Define Player Control Button Images
back_btn_img = PhotoImage(file='images/back.png')
forward_btn_img =  PhotoImage(file='images/forward.png')
play_btn_img =  PhotoImage(file='images/play.png')
pause_btn_img =  PhotoImage(file='images/pause.png')
stop_btn_img =  PhotoImage(file='images/stop.png')


# Create Player Control Buttons
back_button = Button(image=back_btn_img, borderwidth=0, command=previous_song)
forward_button = Button(image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(image=pause_btn_img, borderwidth=0, command=pause)
stop_button =  Button(image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

window.mainloop()