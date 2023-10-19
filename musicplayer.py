from tkinter import * #importing everything from tkinter midule
import pygame #pip install pygame
import os

from time import strftime #imports time
main = Tk()
pygame.mixer.init() #initialize pygame 
n=0

def start_stop():
    global n
    n = n+1
    if n==1:
        song_name=song_listbox.get()
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(0)
    elif(n%2)==0:
        pygame.mixer.music.pause()
    elif(n%2)!=0:
        pygame.mixer.music.unpause()







#create a label
l1= Label(main,text="MUSIC PLAYER BY DHRUTI",font= "times 20")
l1.grid(row=1,column=1)

#Button feature in new variable
b2=Button(main,text = 'o',command=start_stop)
b2.grid(row=4,column=1)

song_list = os.listdir()
song_listbox = StringVar(main)
song_listbox.set('SELECT SONGS')
menu = OptionMenu(main,song_listbox,*song_list)
menu.grid(row=4,column=4)
main.mainloop()


