import tkinter as tk
from tkinter import messagebox
import ui as ui



def close_root_app():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def close_budget_root_app():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        budget_root.destroy()

def quit_application():
    root.destroy()


def open_start_window():
    root.withdraw()
    start_window = tk.Toplevel(root)
    start_window.protocol("WM_DELETE_WINDOW", close_root_app)
    start_window.title("Budget IT")

    title = tk.Label(start_window, text="Budget IT",
                            font=("default", 20), padx=50, pady=15)
    title.pack()

    frame = tk.LabelFrame(start_window, bd=0)
    frame.pack(pady=15)

    login_button = tk.Button(frame, text="Login", font=("default",14),
                                    width=10, command=lambda: go_to_login_window(start_window))
    login_button.grid(row=0, column=0)

    about_button = tk.Button(frame, text="About", font=("default", 14),
                                width=10)
    about_button.grid(row=1, column=0)

    quit_button = tk.Button(frame, text="Quit", font=("default", 14),
                            width=10, command=quit_application) 
    quit_button.grid(row=2, column=0)
    
def open_login_window():
    login_window = tk.Toplevel(root)
    login_window.protocol("WM_DELETE_WINDOW", close_root_app)
    login_window.title("Login Page")
    login_window.geometry("400x200")

    
    # Your login window creation code here
    username_label = tk.Label(login_window, text="Username:",
                                font=("default", 11))
    username_label.grid(row=1, column=1)

    username_entry = tk.Entry(login_window)
    username_entry.grid(row=1, column=2)

    password_label = tk.Label(login_window, text="Password:",
                              font=("default", 11))
    password_label.grid(row=2, column=1)

    password_entry = tk.Entry(login_window)
    password_entry.grid(row=2, column=2)

    login_button = tk.Button(login_window, text="Login", command=lambda: root.destroy())
    login_button.grid(row=1, column=3, rowspan=2, columnspan=2)


    back_button = tk.Button(login_window, text="Back",
                            command=lambda: back_to_start_window(login_window))
    back_button.grid(row=3, column=1, pady=15)

def back_to_start_window(window):
    window.destroy()
    open_start_window()

def go_to_login_window(window):
    window.destroy()
    open_login_window()

def open_budget_window():
    budget_root.withdraw()
    budget_window = tk.Toplevel()
    budget_window.protocol("WM_DELETE_WINDOW", close_budget_root_app)
    budget_window.title('Budget Overview')
    #Today's date
    today_label = tk.Label(budget_window, text="12, November, 2023")
    today_label.grid(row=0,column=0)




#main application
root = tk.Tk()
current_window = root
open_start_window()
#after user verification open budget overview
root.protocol("WM_DELETE_WINDOW", close_root_app)
root.mainloop()

budget_root = tk.Tk()
budget_root.protocol("WM_DELETE_WINDOW", close_budget_root_app)
open_budget_window()
budget_root.mainloop()

