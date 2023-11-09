#https://www.youtube.com/watch?v=knUHd8ZGyiM&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=16
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('slider')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()


def slide():
    my_label= Label(root, text=horizontal.get())
    my_label.pack()
    root.geometry(str(horizontal.get()) + "x400")

horizontal = Scale(root, from_=0, to=400, orient="horizontal")
horizontal.pack()



my_btn = Button(root, text="click me", command=slide)
my_btn.pack()

root.mainloop()