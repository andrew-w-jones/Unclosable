#!bin/python3
from random import seed
from random import randint
from tkinter import *
import tkinter as tk


def mkwin(txt):
    window = tk.Tk()
    window.title("UNCLOSABLE WINDOW")
    label = tk.Label(window,bg='black',fg='white',width=200,height=50,text=txt,font=('Helvetica', 80))
    label.pack(fill=tk.BOTH,expand=True)
    window.mainloop()
times_closed=0




i=1
while i == 1:
    text = '- Good luck -\n- closing this -\n- window -\n--------------\nTimes failed: '+str(times_closed)
    mkwin(text)
    i=1
    times_closed+=1
    print("YOU WILL NEVER SUCCEED")