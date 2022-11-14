
from tkinter import *
import tkinter as tk
import time as tm
from time import strftime

#Colors
BLACK = "#000000"
WHITE = "#FFFFFF"
TEXT_COLOR = "#009900"
GRAY = '#F00000'

#Fonts
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

#Creating a gui
root = Tk()
root.title('Botis Command prompt')
root.resizable(height = 0, width = 0) #prevents resizing

#Adds icon photo
photo = tk.PhotoImage(file = r'botis_logo.png')
root.wm_iconphoto(False, photo)

#Top lable / title / Adding time
def time_lable():
    current_time = strftime('%H:%M:%S %p')
    lable_1.config(text=f"Botis command prompt\n{current_time}")
    lable_1.after(1000,time_lable)
lable_1 = Label(root, bg=BLACK, fg=WHITE, font=FONT_BOLD, pady=10, width=30, height=2)
lable_1.grid(column=0, columnspan=2,sticky='we')

#Window for displaying messages 
txt = Text(root, bg=BLACK, fg=WHITE, font=FONT, width=30)
txt.grid(row=1, column=0, columnspan=2,sticky='we')

#Entry field view
e = Entry(root, bg=BLACK, fg=WHITE, font=FONT, width=30)
e.grid(row=2, column=0,sticky='we')


#class for sending messages either by pressing enter or button
class send():
    def send_return(event):
        msg = "You: " + e.get()
        txt.insert(END, "\n" + msg)
        e.delete(0, END)
        print(msg[5:])
        return msg[5:]

    def send_butt():
        msg = "You: " + e.get()
        txt.insert(END, "\n" + msg)
        e.delete(0, END)
        print(msg[5:])
        return msg[5:]

send_by_but = Button(root, text="Send", font=FONT_BOLD, bg=WHITE,command=send.send_butt).grid(row=2, column=1,sticky='we')
root.bind('<Return>', send.send_return)

time_lable()
root.mainloop()
    




