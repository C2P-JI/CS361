#https://www.youtube.com/watch?v=uqJZWLlnSqs&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=12
from tkinter import * 
from PIL import ImageTk, Image

root = Tk()
root.title('Radio Buttons')

#r = IntVar()  #tkinter way of tracking change in a variable
#if Radio Button variable=r, value = "string" then use r=StringVar()
#r.set("2") #set r to 2

#creating a list of radiobuttons
MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack() 


#simple two radio butt             #declaring variable
#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 1", variable=r, value=2, command=lambda: clicked(r.get())).pack()

#myLabel = Label(root, text=pizza.get())
#myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

mainloop()