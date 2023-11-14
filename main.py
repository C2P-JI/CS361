import tkinter as tk
from tkinter import messagebox
import rpyc
import ui_login as ui_login_func


# def close_root_app():
#     if messagebox.askokcancel("Quit", "Do you want to quit?"):
#         root.destroy()

# def close_budget_root_app():
#     if messagebox.askokcancel("Quit", "Do you want to quit?"):
#         budget_root.destroy()

# def quit_app():
#     root.destroy()


# def open_start_window():
#     root.withdraw()
#     start_window = tk.Toplevel(root)
#     start_window.protocol("WM_DELETE_WINDOW", close_root_app)
#     start_window.title("Budget IT")

#     title = tk.Label(start_window, text="Budget IT",
#                             font=("default", 20), padx=50, pady=15)
#     title.pack()

#     frame = tk.LabelFrame(start_window, bd=0)
#     frame.pack(pady=15)

#     login_button = tk.Button(frame, text="Login", font=("default",14),
#                                     width=10, command=lambda: to_login_window(start_window))
#     login_button.grid(row=0, column=0)

#     about_button = tk.Button(frame, text="About", font=("default", 14),
#                                 width=10)
#     about_button.grid(row=1, column=0)

#     quit_button = tk.Button(frame, text="Quit", font=("default", 14),
#                             width=10, command=quit_app) 
#     quit_button.grid(row=2, column=0)
    
# def open_login_window():
#     login_window = tk.Toplevel(root)
#     login_window.protocol("WM_DELETE_WINDOW", close_root_app)
#     login_window.title("Login Page")
#     login_window.geometry("400x200")

    
#     # Your login window creation code here
#     username_label = tk.Label(login_window, text="Username:",
#                                 font=("default", 11))
#     username_label.grid(row=1, column=1)

#     username_entry = tk.Entry(login_window)
#     username_entry.grid(row=1, column=2)

#     password_label = tk.Label(login_window, text="Password:",
#                               font=("default", 11))
#     password_label.grid(row=2, column=1)

#     password_entry = tk.Entry(login_window)
#     password_entry.grid(row=2, column=2)

#     login_button = tk.Button(login_window, text="Login")
#     login_button.grid(row=1, column=3, rowspan=2, columnspan=2)

#     new_user_button = tk.Button(login_window, text="New User Regristration",
#                                 font=("default", 11), 
#                                 command=lambda: to_new_user_regristration(login_window))
#     new_user_button.grid(row=3, column=2)

#     back_button = tk.Button(login_window, text="Back",
#                             command=lambda: to_start_window(login_window))
#     back_button.grid(row=3, column=1, pady=15)

# def new_user_service(username, password, re_password):
#     conn = rpyc.connect("localhost", 18861)
#     try:
#         success = conn.root.exposed_add_user(username, password, re_password)
#         if success is True:
#             quit_app()
#     finally:
#         conn.close()




# def to_new_user_regristration(previous_window):
#     previous_window.destroy()
#     open_new_user_regristration_window()

# def to_start_window(previous_window):
#     previous_window.destroy()
#     open_start_window()

# def to_login_window(previous_window):
#     previous_window.destroy()
#     open_login_window()





# def open_budget_window():
#     budget_root.withdraw()
#     budget_window = tk.Toplevel()
#     budget_window.protocol("WM_DELETE_WINDOW", close_budget_root_app)
#     budget_window.title('Budget Overview')
#     #Today's date
#     today_label = tk.Label(budget_window, text="12, November, 2023")
#     today_label.grid(row=0,column=0)




#main application

root = tk.Tk()
current_window = root

ui = ui_login_func.UIlogin(root)
ui.open_start_window()
#after user verification open budget overview
#root.protocol("WM_DELETE_WINDOW", close_root_app)
root.mainloop()

#how do I extract what user is loggin in?
user = ui.get_username()
print("user: " + user)

# budget_root = tk.Tk()
# budget_root.protocol("WM_DELETE_WINDOW", close_budget_root_app)
# open_budget_window()
# budget_root.mainloop()
