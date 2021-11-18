import tkinter
from tkinter import *
from tkinter import ttk
import os
import shutil
'''
def stinvar(e1):
    path=e1
    os.chdir(path)'''

def Catagorize():
    folderpath = var.get()
    os.chdir(folderpath)
    os.getcwd()
    os.listdir() # check the files.
    # get the extention
    list_extention = []
    for f1 in os.listdir():
        extention = f1.split(".")[-1]
        list_extention.append(extention)
    print(list_extention)
    list_extention=set(list_extention)
    path=var.get()
    # How we can trnsfer the files in spacific folder.
    for ex in list_extention:
        print(ex,end=",")
        os.mkdir(path + "\\"+ ex)
        for fl in os.listdir():
            if ex in fl:
                shutil.move(fl,path+"\\"+ex)

app=tkinter.Tk()
app.title("File Catagorizer")

mainframe=ttk.Frame(app, padding="4 4 12 12")
mainframe.grid(column=0, row=0 , sticky= (N,W,E,S))
app.columnconfigure(0,weight=1)
app.rowconfigure(0,weight=1)

var=StringVar()
l1=ttk.Label(mainframe,text="File Catagorizer").grid(column=0,row=1,sticky=(N))
l2=ttk.Label(mainframe,text="Enter Folder Path where you want to catagorize file").grid(column=0,row=2,sticky=(W))
e1=ttk.Entry(mainframe,width=50,textvariable=var).grid(column=0,row=3,sticky=(W))
b2=ttk.Button(mainframe,text="Catagorize",width=14,command=Catagorize).grid(column=0,row=4,sticky=(E))

app.mainloop()