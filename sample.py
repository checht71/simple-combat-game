from tkinter import *

import sys

root = Tk()
root.geometry("480x320")
root.title("School Days Left!")

global counter
counter = 30

def upClick():
    global counter
    counter += 1

def downClick():
    global counter
    counter -= 1
    mButton1.config(text = counter, borderwidth = 0, highlightthickness=0, relief='ridge', pady = "100")

mButton1 = Button(text = counter, command = downClick, height = 4000, width = 320, font = ("Monospace", 200))
mButton1.pack()

root.mainloop()