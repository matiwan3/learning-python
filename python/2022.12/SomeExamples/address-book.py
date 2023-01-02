import tkinter as tk
from tkinter import ttk

class AddressBookApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Address Book')
        self.pack()
        self._create_widgets()
        
    def _create_widgets(self):
        tree_view_entries = ["Entry 1", "Entry 2"
                     "Entry 3", "Entry 4"]
        treeview_widget = ttk.Treeview(self.master)
        index = 1
        for entry in tree_view_entries:
            treeview_widget.insert('', 'end', index, text = entry)
            index += 1
        treeview_widget.pack()
        self._create_menus()
        
    def _create_menus(self):
        menu_widget = tk.Menu(self.master)
        file_menu = tk.Menu(menu_widget)
        contact_menu = tk.Menu(menu_widget)
        file_menu.add_command(label="New", command=self._new_address_book)
        file_menu.add_command(label="Open...", command=self._open_address_book)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
                
        