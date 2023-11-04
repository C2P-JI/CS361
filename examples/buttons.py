#source: https://www.youtube.com/watch?v=yuuDJ3-EdNQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=3
from tkinter import *

root=Tk()

def myClick():
    myLabel = Label(root, text="bobby")
    myLabel.pack()

button1 = Button(root, text="button", padx=50, pady=50, command=myClick) #no need for parenthesis when calling myClick functions
button1.pack()

root.mainloop()
