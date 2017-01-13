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

#v = pyvona.create_voice('key1', 'key2')
v = pyvona.create_voice(key1, key2)
v.voice_name = 'Emma'
v.speak('I have been initialized correctly!')

entry.focus()
root.mainloop()
