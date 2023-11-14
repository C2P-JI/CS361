#video 45
from tkinter import *

root = Tk()
root.title('Codemy')
root.geometry("400x400")

def selected():
    myLabel = Label(root, text=clicked.get())
    myLabel.pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack(pady=20)

myButton = Button(root, text="select from list", command=selected)
myButton.pack()

root.mainloop()