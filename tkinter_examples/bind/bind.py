#video 44
from tkinter import *

root = Tk()
root.title('Codemy')
root.geometry("400x400")

def clicker(event):
    myLabel = Label(root, text="You clicked a button" + str(event.x) + " " + str(event.y))
    myLabel.pack()
    

myButton = Button(root, text="Click Me")
myButton.bind("<Enter>", clicker)
myButton.pack(pady=20)

root.mainloop()