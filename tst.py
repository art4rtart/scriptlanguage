from tkinter import *
g_Tk = Tk()
import xml.etree.ElementTree as etree
import urllib.request
import urllib
from tkinter import font

class Data:
    x = 0
    y = 0

def SearchStartStation():
    SearchButton = Button(g_Tk, command=StartStationAction, borderwidth = 5, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=Data.x, y=Data.y)

def StartStationAction():
    Data.x += 10
    print(Data.x)
    SearchStartStation()

SearchStartStation()
StartStationAction()

g_Tk.mainloop()