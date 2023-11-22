import tkinter as tk
from tkinter import ttk
import webbrowser

root = tk.Tk()
root.title('Universal Search Bar')

label1 = ttk.Label(root, text='Query')
label1.grid(row=0, column=0)
entry1 = ttk.Entry(root, width=50)
entry1.grid(row=0, column=1)

btn2 = StringVar()

def callback():
    
    if btn2.get() == 'google':
        webbrowser.open('http://google.com/search?q='+entry1.get())
    elif btn2.get() == 'duck':
        webbrowser.open('http://duckduckgo.com/?q='+entry1.get())

def get(event):

    if btn2.get() == 'google':
        webbrowser.open('http://google.com/search?q='+entry1.get())
    elif btn2.get() == 'duck':
        webbrowser.open('http://duckduckgo.com/?q='+entry1.get())
   
MyButton1 = ttk.Button(root, text='Search', width=10, command=callback)
MyButton1.grid(row=0, column=2)

entry1.bind('<Return>', get)

root.wm_attributes('-topmost', 1)

root.mainloop()

