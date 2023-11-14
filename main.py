import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode



# def add_user(username, password):
#     sql_command = ("INSERT INTO user_login"
#                    "(username, password)"
#                    "VALUES (%s, %s)")
#     values = (username, password)

#     #insert new user
#     cursor.execute(sql_command, values)
#     cnx.commit()

# def user_authentification(target_username, target_password):
#     query = ("SELECT username, password FROM user_login")

#     cursor.execute(query)

#     user_exist = False
#     user_password = False

#     for(username, password) in cursor:
#         if username == target_username:
#             user_exist = True
#             if password == target_password:
#                 user_password = True

        
#     if (user_exist or user_password) == False:
#         print("Login Fail")

#     else:
#         print("Login Success")


add_user_txt(username, password):
    



def close_root_app():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def close_budget_root_app():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        budget_root.destroy()

def quit_app():
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
                                    width=10, command=lambda: to_login_window(start_window))
    login_button.grid(row=0, column=0)

    about_button = tk.Button(frame, text="About", font=("default", 14),
                                width=10)
    about_button.grid(row=1, column=0)

    quit_button = tk.Button(frame, text="Quit", font=("default", 14),
                            width=10, command=quit_app) 
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

    login_button = tk.Button(login_window, text="Login",
                            command=lambda: user_authentification(str(username_entry.get()), str(password_entry.get())))
    login_button.grid(row=1, column=3, rowspan=2, columnspan=2)

    new_user_button = tk.Button(login_window, text="New User Regristration",
                                font=("default", 11), 
                                command=lambda: to_new_user_regristration(login_window))
    new_user_button.grid(row=3, column=2)

    back_button = tk.Button(login_window, text="Back",
                            command=lambda: to_start_window(login_window))
    back_button.grid(row=3, column=1, pady=15)

def open_new_user_regristration_window():
    new_user_window = tk.Toplevel(root)
    new_user_window.protocol("WM_DELETE_WINDOW", close_root_app)
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
                                     font=("default", 11))
    register_user_button.grid(row=2, column=3, padx=20)

    back_button = tk.Button(new_user_window, text="Back",
                             command=lambda: to_login_window(new_user_window))
    back_button.grid(row=4, column=1)



def to_new_user_regristration(previous_window):
    previous_window.destroy()
    open_new_user_regristration_window()

def to_start_window(previous_window):
    previous_window.destroy()
    open_start_window()

def to_login_window(previous_window):
    previous_window.destroy()
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

#establish connection to database
try:
    cnx = mysql.connector.connect(user='root',
                                  password='^69!d0ingSh!tgood',
                                  host='localhost',
                                  database='users')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with you username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = cnx.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS user_login ("
                " `username` varchar(15) NOT NULL,"
                " `password` varchar(30) NOT NULL,"
                " PRIMARY KEY (`username`)"
                ")ENGINE=InnoDB")


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

cursor.close()
cnx.close()