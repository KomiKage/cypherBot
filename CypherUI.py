import sys
import tkinter as tk
from tkinter import *

# ----------------------------

root = tk.Tk()
root.title("Cyphers' brain")
root.geometry('1280x720')
root.configure(bg='#F5F5DC')

# variables-------------------
powerButtonImage = PhotoImage(file = r'images/UI/power.png')
log = open('log.txt','r+')
msg = ''

# defs-------------------------
def yuh():
    global msg
    msg = log.read()
    textBox.insert('end', msg)
    root.after(1,yuh)

# GUI-------------------------

sidePanel = Frame(root,height = 720,width = 200,bg = '#ded0ab')
sidePanel.pack(side=LEFT)

powerButton = tk.Button(image = powerButtonImage, height = 100, width = 100, relief = RAISED, command = yuh)
powerButton.place(x = 50, y = 40)


textBox = Text(root, height=100, width=100)
textBox.pack(side = RIGHT)
textBox.insert('end', msg)

#update

root.after(0,yuh)

root.mainloop()
