#import python gui tikinter module
import tkinter as tk

#create a new window
window = tk.Tk()

#ADDING A WIDGET

#create a label widget
greeting = tk.Label(text="Hello, Tkinter")

#add widget to window one method is the .pack()
greeting.pack()

#runs the program 
window.mainloop()