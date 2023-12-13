import tkinter as tk
from window_manager import WindowManger
from starting_menu import StartingMenu

class UIlogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw() #hide the root window (self) all windows will be managed with Toplevels
        manager = WindowManger()
        starting_menu = StartingMenu(self, manager)
        manager.push_window(starting_menu)
        self.mainloop()