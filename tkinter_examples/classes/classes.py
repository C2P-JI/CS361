from tkinter import *

root = Tk()
root.title("classes")
root.geometry("400x400")

class Elder:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text="Click Me!", command=lambda: self.clicker(master))
        self.myButton.pack(pady=20)

    def clicker(self, master):
        self.new_button = Button(master, text="new button")
        self.new_button.pack(pady=50)

elder = Elder(root)
root.mainloop()