import tkinter as tk

class AboutMenu(tk.Toplevel):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.parent = parent
        self.manager = manager
        self.protocol("WM_DELETE_WINDOW", parent.destroy)
        self.geometry("100x100")
