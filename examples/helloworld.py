from tkinter import *
from tkinter import ttk

root = Tk() #creates an instance of the Tk class, which initialize Tk
            #and associated Tcl interpreter. also makes a root window
            #serves as the main window of the application
frm = ttk.Frame(root, padding = 10) #Creates a frame widget


frm.grid()  #grid() used to specify the relative position of the label
            #within its containing frame widget

#creates a label widget holding static text string
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

#button widget, placed to the right of the label
#it will call destroy() method of the root window
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1,row=0)

#puts everthing on the display and responds to user input until program
#terminantes
root.mainloop()