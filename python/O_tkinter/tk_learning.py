from tkinter import *
from tkinter import Menu
import tkinter 

root = Tk()
root.title("Login app")
root.wm_attributes('-toolwindow', 'True')
root.geometry("300x300")

#create menu bar
menubar = Menu(root)
root.config(menu = menubar)

# create a menu
file_menu = Menu(menubar, tearoff = 0)

# add a menu items to the File menu
file_menu.add_command(label = "New")
file_menu.add_command(label = "Open")
file_menu.add_command(label = "Close")
file_menu.add_separator()

#add a submenu
sub_menu = Menu(file_menu, tearoff = 0)
sub_menu.add_command(label = "Keyboard shortcuts")
sub_menu.add_command(label = "Color themes")

#add the File menu to the menubar
file_menu.add_cascade(label = "Preferences" ,menu = sub_menu)


#add exit menu item
file_menu.add_command(label='Exit', command=root.destroy,)

#add the File menu to the menubar
menubar.add_cascade(label = "Register", menu = file_menu, underline = 0)

#create the help menu
help_menu = Menu(menubar, tearoff = 0)

help_menu.add_command( label = "Welcome")
help_menu.add_command( label = "About...")

#add the help menu to the menu bar
menubar.add_cascade(label = "Help", menu = help_menu)

#register
register_button = tkinter.Button(root, text = "Register", height=3, padx=1)
register_button.pack()

#login
register_login = tkinter.Button(root, text = "Login", height=3, padx=1)
register_login.pack()

#exit
register_exit = tkinter.Button(root, text = "Exit", height=3, padx=1)
register_exit.pack()

root.mainloop()


#Use Menu() to create a new menu,
#Use menu.add_command() method to add a menu item to the menu.
#Use menubar.add_cascade(menu_title, menu) to add a menu to the menubar.
#Use menu.add(submenu_title, submenu) to add a submenu to the menu.