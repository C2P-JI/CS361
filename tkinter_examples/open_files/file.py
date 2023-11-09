#https://www.youtube.com/watch?v=Aim_7fC-inw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=15
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog #use this thang

root = Tk()
root.title('open these files numb nutz')



def open(file_path):
    root.filename = filedialog.askopenfilename(initialdir=file_path, title="Select a file", filetypes=(("all files", "*.*"),))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()
    my_images.append(my_image)

my_images = []

my_btn = Button(root, text="Open File", command=lambda: open(r"c:\\Users\\mocha\\CS361\\tkinter_examples\\new_window\\images"))
my_btn.pack()

root.mainloop()