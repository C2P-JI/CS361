import tkinter as tk
from tkinter import ttk, messagebox
import tkTools as T
from about_menu import AboutMenu
from login_menu import LoginMenu

class StartingMenu(tk.Toplevel):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.parent = parent
        self.manager = manager
        self.protocol("WM_DELETE_WINDOW", parent.destroy)   
        self.geometry("300x200")
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        title_label = ttk.Label(self, text="Expense Tracker", font=("default", 14))
        title_label.grid(row=0, column=0)

        login_button = ttk.Button(self, text="Login", command=self.open_login)
        login_button.grid(row=1, column=0)
        
        about_button = ttk.Button(self, text="About", command=self.open_about)
        about_button.grid(row=2, column=0)

        quit_button = ttk.Button(self, text="Quit", command=self.quit)
        quit_button.grid(row=3, column=0)

    def open_about(self):
        about = AboutMenu(self.parent, self.manager)
        self.manager.push_window(about)
    def open_login(self):
        login = LoginMenu(self.parent, self.manager)
        self.manager.push_window(login)
    def quit(self):
        self.parent.destroy()