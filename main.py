import tkinter as tk


#Settings of the start page
root = tk.Tk()
root.title("Budget it")

'''
# Function: previous_window()
# Parameters:
# Description: return to the previous window
'''
def previous(previous_window, current_window):
    current_window.destroy()
    previous_window.deiconify()
'''
# Function: login_event
# Description: opens to a new window and allows user to login 
# or create a new account to use the budget service
'''
def login_event():
    # Create a new window for the login page
    login_win = tk.Tk()
    login_win.title("Login Page")
    login_win.geometry("400x200")

    #Hide the current window
    root.withdraw()

    # Create widgets for the login page
    username_label = tk.Label(login_win, text="Username:", font=("default", 11))
    username_label.place(x=40, y=20)

    username_entry = tk.Entry(login_win)
    username_entry.place(x=120, y=23)

    password_label = tk.Label(login_win, text="Password:", font=("default", 11))
    password_label.place(x=40, y=50)

    password_entry = tk.Entry(login_win, show="*")  # Password is hidden
    password_entry.place(x=120, y=53)

    login_button = tk.Button(login_win, text="Login", font=("default", 11))
    login_button.place(x=300, y=30)

    new_user_button = tk.Button(login_win, text="New User", font=("default", 11),
                             command=lambda: new_user_event(login_win))
    new_user_button.place(x=175, rely=.5)

    back_button = tk.Button(login_win, text="Back", command=lambda: previous(root, login_win))
    back_button.place(relx=.01, rely=.85)

'''
# Function: new_user_event()
# Parameters:
# Description: Allow for new user regristation. Accessible from Login page
#
'''
def new_user_event(previous_win):
    new_user_win = tk.Tk()
    new_user_win.title("New User")
    new_user_win.geometry("400x200")

    previous_win.withdraw()

    username_label = tk.Label(new_user_win, text="Username:", font=("default", 11))
    username_label.place(x=40, y=20)

    username_entry = tk.Entry(new_user_win)
    username_entry.place(x=120, y=23)

    password_label = tk.Label(new_user_win, text="Password:", font=("default", 11))
    password_label.place(x=40, y=50)

    password_entry = tk.Entry(new_user_win) #, show="*")  # Password is hidden
    password_entry.place(x=120, y=53)

    password_re_label = tk.Label(new_user_win, text="re-enter password:", font=("default", 11))
    password_re_label.place(x=20, y=80)

    password_re_entry = tk.Entry(new_user_win)
    password_re_entry.place(x=150, y = 83)

    create_button = tk.Button(new_user_win, text="Create User", font=("default", 11))
    create_button.place(x=300, y=30)


    back_button = tk.Button(new_user_win, text="Back", command=lambda: previous(previous_win, new_user_win))
    back_button.place(relx=.01, rely=.85)

'''
# Function: budget_overview()
# Parameters: idk yet
# Description: Provides an overview of the user's budget defined by the
# user's personal objective. 
#
# Creator note: This will be created showing the monthly overview 
# there will be a pie chart breaking down where money has went
# an area to input recent transactions
# more to come
'''
def budget_overview():
    return

'''
# Function: new_user_preferences()
# Parameters: idk yet
# Description: The user will select and/or add what catagories they will 
# be used. They will have an option to go for simple, detailed, or custom
#
# Creator note: make the budget_overview first
'''
def new_user_preferences():
    return
'''
# Function: about_event()
# Parambeters:
# Description: Opens a page to infom the user about functionality
# Creator note: complete last
'''
def about_event():
    about_win = tk.Tk()
    about_win.title("About Dummy Driver")
    about_win.geometry("400x200")

    root.withdraw()

    back = tk.Button(about_win, text="Back", command=lambda: previous(root, about_win))
    back.pack()

'''
# Widgets for starting page
'''
title = tk.Label(root, text="Budget IT", font=("default", 20), padx=50, pady=15)
title.pack()
# title.grid(row=1, column=1, columnspan=3)

frame = tk.LabelFrame(root, bd=0)
frame.pack(pady=15)

login = tk.Button(frame, text="Login", font=("default", 14), width=10,
               command=login_event)
login.grid(row=0, column=0)
# login = Button(root, text="login", font=("default", 14),)
# login.grid(row=2, column=2)

about = tk.Button(frame, text="About", font=("default", 14), width=10,
               command=about_event)
about.grid(row=1, column=0)
# about = Button(root, text="About", font=("default", 14))
# about.grid(row=3, column=2)

exit = tk.Button(frame, text="Exit", font=("default", 14), width=10, command=quit)
exit.grid(row=2, column=0)
# exit = Button(root, text="Exit", font=("default", 14))
# exit.grid(row=4, column=2)

root.mainloop()