#https://www.youtube.com/watch?v=4IsLwwb_yDs&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=17
from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('check box example')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get())
    myLabel.pack()


var = StringVar()

c = Checkbutton(root, text= "Check boxes", variable=var, onvalue="On", offvalue="Off")
c.deselect() 
c.pack()

myButton = Button(root, text="Show Selection", command=show)
myButton.pack()


root.mainloop()