from tkinter import *
g_Tk = Tk()
g_Tk.geometry("1000x720+280+30")

photo = PhotoImage(file="sub.gif")  # 디폴트 이미지 파일
imageLabel = Label(g_Tk, image=photo)
imageLabel.place(x=100, y=0)

g_Tk.mainloop()