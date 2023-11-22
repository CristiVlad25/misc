from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from threading import Thread
import pyvona
from keys import *

root = Tk()
root.resizable(0,0)
root.title('Ivona Speech Synthesizer')
img = PhotoImage(file='c:\\users\\cristi\\desktop\\speakb2.png')

def callback():

    v.speak(entry.get('1.0', END))
    entry.delete('1.0', END)

def thr():

    t1 = Thread(target=callback)
    t1.start()

entry = scrolledtext.ScrolledText(root, width=30, height=10, wrap=WORD,
                                  background='#a6f4e7', font='helvetica 12')
entry.grid(row=0, column=0)

button = Button(root, image=img, command=thr, bd=0, overrelief='sunken')
button.grid(row=0, column=1, sticky=N)

#v = pyvona.create_voice('key1', 'key2')
v = pyvona.create_voice(key1, key2)
v.voice_name = 'Emma'

entry.focus()
root.mainloop()
