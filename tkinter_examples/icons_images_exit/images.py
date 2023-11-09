#https://www.youtube.com/watch?v=NoTM8JciWaQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=8
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Learn to code')

#root.iconbitmap('filepath to .ico') #creates the icon image on the top left

my_img = ImageTk.PhotoImage(Image.open("spider.jpeg"))
my_label = Label(image=my_img)
my_label.pack()




button_quit = Button(root, text="Exit program", command=root.quit)

root.mainloop()