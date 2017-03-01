#!/usr/bin/env python3.4

from tkinter import *
from tkinter import ttk
import webbrowser
import speech_recognition as sr
from pygame import mixer
from keys import *

root = Tk()
root.title('Universal Search Bar')
root.iconbitmap('mic.ico')

style = ttk.Style()
style.theme_use('winnative')

photo = PhotoImage(file='microphone.png').subsample(15,15)

label1 = ttk.Label(root, text='Query:')
label1.grid(row=0, column=0)
entry1 = ttk.Entry(root, width=40)
entry1.grid(row=0, column=1, columnspan=4)

btn2 = StringVar()

def callback():
    
    if btn2.get() == 'google':
        webbrowser.open('http://google.com/search?q='+entry1.get())
        
    elif btn2.get() == 'duck':
        webbrowser.open('http://duckduckgo.com/?q='+entry1.get())

    elif btn2.get() == 'amz':
        webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='+entry1.get())

    elif btn2.get() == 'ytb':
        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())

    else:
        pass


def get(event):

    if btn2.get() == 'google':
        webbrowser.open('http://google.com/search?q='+entry1.get())
        
    elif btn2.get() == 'duck':
        webbrowser.open('http://duckduckgo.com/?q='+entry1.get())

    elif btn2.get() == 'amz':
        webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='+entry1.get())

    elif btn2.get() == 'ytb':
        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())

    else:
        pass

def buttonClick():

    mixer.init()
    mixer.music.load('chime1.mp3')
    mixer.music.play()

    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400

entry1.bind('<Return>', get)

MyButton1 = ttk.Button(root, text='Search', width=10, command=callback)
MyButton1.grid(row=0, column=6)

MyButton2 = ttk.Radiobutton(root, text='Google', value='google', variable=btn2)
MyButton2.grid(row=1, column=1, sticky=W)

MyButton3 = ttk.Radiobutton(root, text='Duck', value='duck', variable=btn2)
MyButton3.grid(row=1, column=2, sticky=W)

MyButton4 = ttk.Radiobutton(root, text='Amz', value='amz', variable=btn2)
MyButton4.grid(row=1, column=3)

MyButton5 = ttk.Radiobutton(root, text='Ytb', value='ytb', variable=btn2)
MyButton5.grid(row=1, column=4, sticky=E)

MyButton6 = Button(root, image=photo, command=buttonClick, bd=0, activebackground='#c1bfbf', overrelief='groove', relief='sunken')
MyButton6.grid(row=0, column=5)

entry1.focus()
root.wm_attributes('-topmost', 1)
root.mainloop()
