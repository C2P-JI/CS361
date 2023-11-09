'''
Learning source: https://www.youtube.com/watch?v=BSfbjrqIw20&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=2

'''

from tkinter import *

root = Tk()

#creating a label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Big booty")
#Shoving it onto the screen
myLabel1.grid(row = 0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()