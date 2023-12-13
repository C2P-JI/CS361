import tkinter as tk
from tkinter import messagebox, ttk
import tkTools as T
from partner_service import CredentialCheck
from new_user import NewUser

class LoginMenu(tk.Toplevel):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.parent.destroy)
        self.manager = manager
        self.title("Login")
        self.create_widgets()

    def create_widgets(self):
        username_label = T.create_label(self, "Username", 1, 1)
        username_entry = T.create_entry(self, 25, 1, 2)
        password_label = T.create_label(self, "Password", 2, 1)
        password_entry = ttk.Entry(self, show='*')
        password_entry.grid(row=2, column=2)
        login_button = T.create_button(self, "Login", 
                                       lambda: self.credential_check_service(username_entry.get(), 
                                                                        password_entry.get()),
                                                                        1, 3)
        new_user_button = T.create_button(self, "New User Regristration", 
                                          lambda: self.open_new_user_regristration(), 3, 2)
        back_button = T.create_button(self, "Back", lambda: self.go_back(), 3, 1)

    def go_back(self):
        self.manager.pop_window()

    def open_new_user_regristration(self):
        user = NewUser(self.parent, self.manager)
        self.manager.push_window(user)


    def write_username(self, username):
        with open("user.txt", 'w') as file:
            file.write(username)


    
    def result_action(self, username, result):
        if result == "access granted":
            self.write_username(username)
            self.parent.destroy()
        else:
            messagebox.showerror("Error", result)
    
    #previous action: user clicks button login in LeginMenu
    def credential_check_service(self, username, password):
        credential_check = CredentialCheck(username, password)
        result = credential_check.run_service()
        self.result_action(username, result)


