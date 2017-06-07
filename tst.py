from tkinter import *
window = Tk()

l1 = Label(window, text="달러")
l2 = Label(window, text="원")
l1.pack()
l2.pack()

def process():
    print(e1.get())


e1 = Entry(window)
e1.pack()

b1 = Button(window, command = process)
b1.pack()


window.mainloop()
