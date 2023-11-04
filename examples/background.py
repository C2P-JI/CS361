#learning source: https://www.youtube.com/watch?v=WurCpmHtQc4
#import customtkinter as ctk
import tkinter as tk

root = tk.Tk()
root.title("Dummy Driver")
root.geometry("800x600")
#Load the image 
background_image = tk.PhotoImage(file="pic.gif")

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


'''
#create a label
my_label = tk.Label(root, image=background_image)
my_label.place(x=0, y=0, relwidth=1, relheight=1)


my_text = tk.Label(root, text="Dummy Driver", font=("Helvetica", 50), fg="white")
my_text.pack(pady=150)

#create a frame
my_frame=tk.Frame(root)
my_frame.pack(pady=20)

#Add some buttons 
my_button1 = tk.Button(my_frame, text="Exit")
my_button1.grid(row=0, column=0, padx=20)

my_button2 = tk.Button(my_frame, text="Start")
my_button2.grid(row=0, column=1, padx=20)

my_button3 = tk.Button(my_frame, text="Reset")
my_button3.grid(row=0, column=2, padx=20)

# canvas = tk.Canvas(root, width = background_image.width(), height=background_image.height())
# canvas.pack()

# canvas.create_image(0,0, anchor=tk.NW, image=background_image)

# label=tk.Label(canvas, text="Dummy Driver", font=("default",20))
# label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


'''
root.mainloop()