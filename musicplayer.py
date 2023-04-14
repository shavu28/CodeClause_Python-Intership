from tkinter import *
import pygame
import os
from tkinter import filedialog

root=Tk()
root.title("Music Player")
root.geometry("750x500")

pygame.mixer.init()

def add_song():
    song=filedialog.askopenfilename(initialdir="C:\music",title="choose a song", filetypes=(( "mp3 Files","*.mp3"), ))

    song=song.replace("C:/music","")
    song=song.replace(".mp3","")
    
    song_box.insert(END,song)

def add_many_songs():
     songs=filedialog.askopenfilenames(initialdir="C:\music",title="choose a song", filetypes=(( "mp3 Files","*.mp3"), ))

     for song in songs:
          song=song.replace("C:/music","")
          song=song.replace(".mp3","")
         
          song_box.insert(END,song)

def play():
    song= song_box.get(ACTIVE)
    song=f'c:/music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

global paused
paused=False

def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        #unpause
        pygame.mixer.music.unpause()
        paused=False
    else:
        pygame.mixer.music.pause()
        paused=True
     
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

def next_song():
    next_one= song_box.curselection()
   
    next_one= next_one[0]+1
    song= song_box.get(next_one)

    song= f'c:/music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
#clear active bar
    song_box.selection_clear(0,END)

#activate new one
    song_box.activate(next_one)
#set active song
    song_box.selection_set(next_one,last=None)

def previous_song():

    next_one= song_box.curselection()
   
    next_one= next_one[0]-1
    song= song_box.get(next_one)

    song= f'c:/music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
#clear active bar
    song_box.selection_clear(0,END)

#activate new one
    song_box.activate(next_one)
#set active song
    song_box.selection_set(next_one,last=None)
    
    

song_box = Listbox(root, bg="black", fg="green", width=75, selectbackground="grey", selectforeground="black")
song_box.pack(pady=20)

play_btn_img=PhotoImage(file="F:\\Internships\\Code_Clause\\New folder\\play.png")
pause_btn_img=PhotoImage(file="F:\\Internships\\Code_Clause\\New folder\\pause.png")
stop_btn_img=PhotoImage(file="F:\\Internships\\Code_Clause\\New folder\\stop.png")
rewind_btn_img=PhotoImage(file="F:\\Internships\\Code_Clause\\New folder\\rewind.png")
forward_btn_img=PhotoImage(file="F:\\Internships\\Code_Clause\\New folder\\forward.png")

control_frame= Frame(root)
control_frame.pack()

play_btn=Button(control_frame, image=play_btn_img, borderwidth=0,command=play)
pause_btn=Button(control_frame, image=pause_btn_img, borderwidth=0,command=lambda:pause(paused))
stop_btn=Button(control_frame, image=stop_btn_img, borderwidth=0,command=stop)
rewind_btn=Button(control_frame, image=rewind_btn_img, borderwidth=0,command=previous_song)
forward_btn=Button(control_frame, image=forward_btn_img, borderwidth=0,command=next_song)

rewind_btn.grid(row=0,column=0,padx=7,pady=10)
play_btn.grid(row=0,column=1,padx=7,pady=10)
pause_btn.grid(row=0,column=2,padx=7,pady=10)
forward_btn.grid(row=0,column=3,padx=7,pady=10)
stop_btn.grid(row=0,column=4,padx=7,pady=10)

# Create Menu

my_menu=Menu(root)
root.config(menu=my_menu)

#add songs

add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add a song to playlist",command=add_song)

#add many songs to playlist

add_song_menu.add_command(label="Add many songs to playlist",command=add_many_songs)



root.mainloop()
