#https://www.youtube.com/watch?v=3E_fK5hCUnI&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=18
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('drop down menu example')
root.geometry("400x400")

#Drop Down Boxes

def show():
    myLabel = Label(root, text=clicked.get()).pack()


options=[
    "Monday", 
    "Tuesday",
    "Wednesday", 
    "Thursday", 
    "Friday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options) # * is important to seperate the list into selectable options
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()