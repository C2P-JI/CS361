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
my_canvas.create_text(400, 250, text="Dummy Driver", font=("Helvetica", 50)) #fill to change font color

#add some buttons
login = tk.Button(root, text="login")
guest = tk.Button(root, text="guest")
exit = tk.Button(root, text="Exit")

login_window=my_canvas.create_window(10, 10, anchor="nw", window=login)
guest_window=my_canvas.create_window(50, 10, anchor="nw", window=guest)
exit_window=my_canvas.create_window(130, 10, anchor="nw", window=exit)

root.mainloop()
