#https://www.youtube.com/watch?v=_auZ8TTkojQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=11
from tkinter import * #pip install tkinter?
from PIL import ImageTk, Image #pip install Pillow

root = Tk()
root.title('Frame example')
#root.iconbitmap('file path') 

frame = LabelFrame(root, text="This is my frame...", padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click here")
b.grid(row=0, column=0)

b2 = Button(frame, text="booby")
b2.grid(row=1, column=1)



root.mainloop()