#Since this uses some code from my oszloader, I've kept the imports same.

import getpass
import os
import tkinter as wm
import shutil
import time
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import json

top = wm.Tk()
top.geometry("270x140")
top.title('Folder Lister')

eres = wm.Label(top, bd=5, width = 24)
eres.place(x=10, y=20)
eres["text"]= "Folder Name"
e1 = wm.Entry(top, bd=5, width=24)
e1.place(x=10, y=50)


eshow = wm.Label(top, bd=5, width = 24)
eshow.place(x=30, y=110)



def set_text(anan, owo):
	#This sets text for entry objects (anan is entry)
	anan.delete(0,wm.END)
	anan.insert(0,owo)

def fDialog():
    path = askdirectory(title='Select Folder')
    set_text(e1, path)


def runA():
    sancheck = True 
    if not os.path.isdir(e1.get()):
        messagebox.showwarning(title="Bad Input", message="Folder selected invalid!")
        sancheck=False

    #I know, this is a primitive way to handle this error. I also don't care.
    if sancheck:
        filenames= os.listdir (e1.get()) # get all files' and folders' names in the entry
        result = []
        for filename in filenames: # loop through all the files and folders
            if os.path.isdir(os.path.join(os.path.abspath(e1.get()), filename)): # check whether the current object is a folder or not
                result.append(filename)
        result.sort()

        f= open('list.txt','w' ,encoding='utf-8')
        for filename in result:
            f.write("%s \n"%(filename))
        f.close()
        eshow["text"] = "List exported as list.txt"
    
'''X=185 button'''
fPick=wm.Button(top,text="...",command=lambda: fDialog())
fPick.place(x=185, y=50)

mbutton=wm.Button(top,text="Run",command=lambda: runA())
mbutton.place(x=225, y=50)
top.mainloop()