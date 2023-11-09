#source: https://www.youtube.com/watch?v=7A_csP9drJw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=4

from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="black", fg="lightgreen")
e.pack()
e.get()


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack()

root.mainloop()