import tkinter as tk
from tkinter import messagebox
import tkTools as T
from user_regristration import UserRegristration
from window_manager import WindowManger

class NewUser(tk.Toplevel):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.parent = parent
        self.manager = manager
        self.protocol("WM_DELETE_WINDOW", self.parent.destroy)
        self.title("New User Regristration")
        self.create_widgets()

    def create_widgets(self):
        username_label = T.create_label(self, "Username", 1, 1)
        username_entry = T.create_entry(self, 25, 1, 2)
        password_label = T.create_label(self, "Password", 2, 1)
        password_entry = T.create_entry(self, 25, 2, 2)
        re_password_label = T.create_label(self, "Match Password", 3, 1)
        re_password_entry = T.create_entry(self, 25, 3, 2)
        
        #contains command to create new user
        register_button = T.create_button(self, "Register", lambda: self.new_user(
                                                                str(username_entry.get()),
                                                                str(password_entry.get()),
                                                                str(re_password_entry.get())),
                                                                2, 3)
        back_button = T.create_button(self, "Back", lambda: self.go_back(), 4, 1)


    def new_user(self, username, password, re_password):
        if self.valid_username(username):
            if self.valid_password(password, re_password):
                self.create_new_user(username, password)

    
    def valid_username(self, new_username):
        valid = True
        file = open("user_login.txt", 'r')

        for index, username in enumerate(file, start=1):
            if index % 2 == 1:
                if username.strip() == new_username:
                    valid = False
                    messagebox.showerror("Error", "Username Is Taken")
        file.close()
        return valid
    
    def valid_password(self, password, re_password):
        if password == re_password:
            return True
        else:
            messagebox.showerror("Error", "Passwords do not match")
            return False
        
    def create_new_user(self, username, password):
        self.write_username_password(username, password)
        #clear stack list?
        register = UserRegristration(self.parent, self.manager, username)
        self.manager.push_window(register)


    def write_username_password(self, username, password):
        file = open(r"user_login.txt", "a")
        upload = username + "\n" + password + "\n"
        file.write(upload)
        file.close()
    

    def go_back(self):
        self.manager.pop_window()

