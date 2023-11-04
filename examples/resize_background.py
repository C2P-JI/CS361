#learning source: https://www.youtube.com/watch?v=xiGQD2J47nA
#import customtkinter as ctk
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Dummy Driver")
root.geometry("800x600")
#Load the image 
background_image = ImageTk.PhotoImage(file="pic.gif")   #can use differnt types of photos

#create a canvas
my_canvas = tk.Canvas(root, width = 800, height=600)
my_canvas.pack(fill="both", expand=True)

#set image in canvas
my_canvas.create_image(0,0, image=background_image, anchor="nw")


#Add a label
my_canvas.create_text(400, 250, text="Welcome!", font=("Helvetica", 50)) #fill to change font color

#add some buttons
button1 = tk.Button(root, text="Start")
button2 = tk.Button(root, text="Reset Score")
button3 = tk.Button(root, text="Exit")

button1_window=my_canvas.create_window(10, 10, anchor="nw", window=button1)
button2_window=my_canvas.create_window(50, 10, anchor="nw", window=button2)
button3_window=my_canvas.create_window(130, 10, anchor="nw", window=button3)

def resizer(e):
    global bg1, resized_bg, new_bg
    #open our image
    bg1 = Image.open("pic.gif")
    #resize the image
    resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
    #define our image again
    new_bg = ImageTk.PhotoImage(resized_bg)
    #Add it back to the canvas
    my_canvas.create_image(0,0, image=new_bg, anchor="nw")

root.bind('Configure', resizer)

root.mainloop()