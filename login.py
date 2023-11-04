import tkinter as tk    #import the tkinter library

#create main application window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x200")

#implement the login function
def login():
    username = username_entry.get()
    password = password_entry.get()

    #add your authentification logic here
    if username == "example" and password == "password":
        result_label.config(text="Login successful")
        #add code to open the main application or game here
    else:
        result_label.config(text="Invalid username or password")

#design the login form
username_label = tk.Label(root, text = "Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*") #password is hidden
password_entry.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

root.mainloop()



