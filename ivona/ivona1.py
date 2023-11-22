from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from threading import Thread
import pyvona
from keys import *

root = Tk()
root.title('Ivona Speech Synthesizer')

def callback():

    #ivona will speak from here
    pass

def thr():

    #threading - so that our main app does not freeze
    pass

entry = scrolledtext.ScrolledText(root, width=30, height=10, wrap=WORD)
entry.grid(row=0, column=0)

button = ttk.Button(root, text='Speak', command=thr)
button.grid(row=0, column=1, sticky=N)

#placeholder for ivona

entry.focus()
root.mainloop()
