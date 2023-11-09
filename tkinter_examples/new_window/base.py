#https://www.youtube.com/watch?v=qC3FYdpJI5Y&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=14
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('base')

def open(image_path):
    top = Toplevel()
    top.title('My second window')
    my_img = ImageTk.PhotoImage(Image.open(image_path))
    my_label = Label(top, image=my_img).pack()
    #append my_img object to a list to keep a reference to it
    #this is a work around, video suggests using global variables
    my_images.append(my_img)
    btn2 = Button(top, text="close window", command=top.destroy).pack()


my_images = []

btn = Button(root, text="Open Second Window", command=lambda:open("images/3.jpg")).pack()




mainloop()