import rpyc
from tkinter import messagebox

class UserService(rpyc.Service):
    def on_connect(self, conn):
        print("Client connected")
    
    def on_disconnect(self, conn):
        print("Client disconnected")

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


    def exposed_add_user(self, username, password, re_password):
        if self.valid_username(username):
            if self.valid_password(password, re_password):
                file = open(r"user_login.txt", "a")
                upload = username + "\n" + password + "\n"
                file.write(upload)
                file.close()
                return True
            
        return False



if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(UserService, port=18861)
    server.start()