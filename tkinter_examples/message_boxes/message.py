#https://www.youtube.com/watch?v=S3AaSwpb5GE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=13
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox #must use this new

root = Tk()
root.title('message box')

#different info boxes
#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello world")
    Label(root, text=response).pack()
    # if response == 1:
    #     Label(root, text="You clicked yes").pack()
    # else:
    #     Label(root, text="You clicked no").pack()

Button(root, text="Popup", command=popup).pack()


mainloop()