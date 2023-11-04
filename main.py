import tkinter as tk
from login_functions import login_event

#Settings of the start page
root = tk.Tk()
root.title("Dummy Driver")
root.geometry("800x600")

#Load the image 
background_image = tk.PhotoImage(file="pic.gif")

#create a canvas
start_canvas = tk.Canvas(root, width = 800, height=600)
start_canvas.pack(fill="both", expand=True)

#set image in canvas
start_canvas.create_image(0,0, image=background_image, anchor="nw")

#Add a label
start_canvas.create_text(400, 150, text="Dummy Driver", font=("Helvetica", 50), anchor="center") #fill to change font color

#lamda function creates an anonymous function that takes no arguments and 
#calls 'login_event(root)'. Theis way root is passed correctly
login = tk.Button(root, text="login", command=lambda: login_event(root))
guest = tk.Button(root, text="guest")
exit = tk.Button(root, text="Exit")
about = tk.Button(root, text="About")


login_window=start_canvas.create_window(400, 200, anchor="center", window=login)
guest_window=start_canvas.create_window(400, 230, anchor="center", window=guest)
exit_window=start_canvas.create_window(400, 280, anchor="center", window=exit)
about = start_canvas.create_window(10, 580,anchor="w", window = about)

root.mainloop()