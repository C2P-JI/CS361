import tkinter as tk

def open_login_page():
    #close the main window
    root.destroy()

    # Create a new window for the login page
    login_window = tk.Tk()
    login_window.title("Login Page")
    login_window.geometry("800x600")

    # Create widgets for the login page
    username_label = tk.Label(login_window, text="Username:")
    username_label.pack()

    username_entry = tk.Entry(login_window)
    username_entry.pack()

    password_label = tk.Label(login_window, text="Password:")
    password_label.pack()

    password_entry = tk.Entry(login_window, show="*")  # Password is hidden
    password_entry.pack()

    login_button = tk.Button(login_window, text="Login")
    login_button.pack()

root = tk.Tk()
root.title("Login App")
root.geometry("800x600")

login_button = tk.Button(root, text="Login", command=open_login_page)
login_button.pack()

root.mainloop()
