import tkinter as tk
from tkinter import messagebox
import rpyc


class UIlogin:
    def __init__(self, root):
        self.master = root
        self.user = ""

    def get_username(self):
        return self.user
    
    def close_root_app(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.destroy()

    def quit_app(self):
        self.master.destroy()


    def to_new_user_regristration(self, previous_window):
        previous_window.destroy()
        self.open_new_user_regristration_window()

    def to_start_window(self, previous_window):
        previous_window.destroy()
        self.open_start_window()

    def to_login_window(self, previous_window):
        previous_window.destroy()
        self.open_login_window()



    def open_start_window(self):
        self.master.withdraw()
        start_window = tk.Toplevel(self.master)
        start_window.protocol("WM_DELETE_WINDOW", self.close_root_app)
        start_window.title("BudgetIT")

        title = tk.Label(start_window, text="Budget IT",
                                font=("default", 20), padx=50, pady=15)
        title.pack()

        frame = tk.LabelFrame(start_window, bd=0)
        frame.pack(pady=15)

        login_button = tk.Button(frame, text="Login", font=("default",14),
                                        width=10, command=lambda: self.to_login_window(start_window))
        login_button.grid(row=0, column=0)

        about_button = tk.Button(frame, text="About", font=("default", 14),
                                    width=10)
        about_button.grid(row=1, column=0)

        quit_button = tk.Button(frame, text="Quit", font=("default", 14),
                                width=10, command=self.quit_app) 
        quit_button.grid(row=2, column=0)

    def open_login_window(self):
        login_window = tk.Toplevel(self.master)
        login_window.protocol("WM_DELETE_WINDOW", self.close_root_app)
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

        login_button = tk.Button(login_window, text="Login")
        login_button.grid(row=1, column=3, rowspan=2, columnspan=2)
        # Time to make command for login authentification

        new_user_button = tk.Button(login_window, text="New User Regristration",
                                    font=("default", 11), 
                                    command=lambda: self.to_new_user_regristration(login_window))
        new_user_button.grid(row=3, column=2)

        back_button = tk.Button(login_window, text="Back",
                                command=lambda: self.to_start_window(login_window))
        back_button.grid(row=3, column=1, pady=15)

    def new_user_service(self, username, password, re_password):
        conn = rpyc.connect("localhost", 18861)
        try:
            success = conn.root.exposed_add_user(username, password, re_password)
            if success != False:
                self.user = username
                self.quit_app()
                self.create_user_db(username)
        finally:
            conn.close()

        # open windows to get user_information
        # catagories wanted
        # Current income
        # Current rent
        # CUrrent bills
        # etc etc or just skip to main menu and
        # fill in as they go
        

    def create_user_db(self, username):
        conn = rpyc.connect("localhost", port = 18862)
        try:
            conn.root.exposed_create_db(username)
        finally:
            conn.close()

        

    def open_new_user_regristration_window(self):
        new_user_window = tk.Toplevel(self.master)
        new_user_window.protocol("WM_DELETE_WINDOW", self.close_root_app)
        new_user_window.title("New User Regristration")

        username_label = tk.Label(new_user_window, text="Username", font=("defautl",11))
        username_label.grid(row=1, column=1)

        username_entry = tk.Entry(new_user_window)
        username_entry.grid(row=1, column=2)

        password_label = tk.Label(new_user_window, text="Password", font=("default", 11))
        password_label.grid(row=2, column=1)

        password_entry = tk.Entry(new_user_window)
        password_entry.grid(row=2, column=2)

        re_password_label = tk.Label(new_user_window, text="re-enter password", 
                                    font=("default", 11))
        re_password_label.grid(row=3, column=1)

        re_password_entry = tk.Entry(new_user_window)
        re_password_entry.grid(row=3, column=2)

        register_user_button = tk.Button(new_user_window, text="Register", 
                                        font=("default", 11), 
                                        command=lambda: self.new_user_service(str(username_entry.get()),
                                                                str(password_entry.get()),
                                                                str(re_password_entry.get())))
        register_user_button.grid(row=2, column=3, padx=20)

        back_button = tk.Button(new_user_window, text="Back",
                                command=lambda: self.to_login_window(new_user_window))
        back_button.grid(row=4, column=1)
        


# root = tk.Tk()

# ui = UIlogin(root)

# ui.open_start_window()

# root.mainloop()
# user = ui.get_username()
# print("user:" + user) #awesome we got the user now we can create a csv and 
#                         #collect and store data 

