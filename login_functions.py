import tkinter as tk


def login_event(root):
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

    new_user_button = tk.Button(login_window, text="New User")
    new_user_button.pack()
