import tkinter as tk
import mysql.connector
from mysql.connector import errorcode


try:
    cnx = mysql.connector.connect(user='root', 
                                password='^69!d0ingSh!tgood',
                                host='localhost',
                                database='users')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with you user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    #create a cursor for the db
    cursor = cnx.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS user_login ("
                " `username` varchar(15) NOT NULL,"
                " `password` varchar(30) NOT NULL,"
                " PRIMARY KEY (`username`)"
                ")ENGINE=InnoDB")

# #Checks the user_info table
# cursor.execute("SELECT * FROM user_login")
# result = cursor.fetchall()
# for x in result:
#      print(x)



#Settings of the start page
root = tk.Tk()
root.title("Budget it")

# host = "localhost"
# user = "root"
# password = "^69!d0ingSh!tgood"

#Establish a connection to the MySQL server
#cnx = mysql.connector.connect(host=host, user=user, password=password)

#create a cursor ovject to execute SQL statments
#cursor = cnx.cursor()

#database name
DB_NAME = 'users'

#Create the database if it doesn't exist


# TABLES = {}

# TABLES['user_login'] =(
#     "CREATE TABLE 'user_login' ("
#     " 'username' varchar(15) NOT NULL,"
#     " 'password' varchar(30) NOT NULL"
#     " PRIMARY KEY ('username')"
#     ")ENGINE=InnoDB")


'''
# Function: create_database(cursor):
# Parameters: cursor - how to navigate the database
# Description: create new databases
'''
# def create_database(cursor):
#     try:
#         cursor.execute(
#             "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
#     except mysql.connector.Error as err:
#         print("Failed creating database: {}".format(err))
#         exit(1)

# try:
#     cursor.execute("USE {}".format(DB_NAME))
# except mysql.connector.Error as err:
#     print("Database {} does not exists.".format(DB_NAME))
#     if err.errno==errorcode.ER_BAD_DB_ERROR:
#         create_database(cursor)
#         print("Database {} created successfully.".format(DB_NAME))
#         cnx.database = DB_NAME
#     else:
#         print(err)
#         exit(1)

# for table_name in TABLES:
#     table_description = TABLES[table_name]
#     try:
#         print("Creating table {}: ".format(table_name), end='')
#         cursor.execute(table_description)
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#             print("already exists.")
#         else:
#             print("OK")
# cnx.commit()
# cursor.close()
# cnx.close()

def add_user(username, password):
        sql_command = ("INSERT INTO user_login"
                    "(username, password)"
                    "VALUES (%s, %s)")
        values = (username.get(),
                password.get())
        
        #insert new user
        cursor.execute(sql_command, values)
        cnx.commit()



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

    login_button = tk.Button(login_win, text="Login", font=("default", 11),
                             command=lambda: budget_overview(login_win))
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

        create_button = tk.Button(new_user_win, text="Create User", font=("default", 11),
                                command=lambda: add_user(username_entry, password_entry))
        create_button.place(x=300, y=30)


        back_button = tk.Button(new_user_win, text="Back", command=lambda: previous(previous_win, new_user_win))
        back_button.place(relx=.01, rely=.85)


'''
# Function: budget_overview()
# Parameters: previous_window - 
# Description: Provides an overview of the user's budget defined by the
# user's personal objective. 
#
# Creator note: This will be created showing the monthly overview 
# there will be a pie chart breaking down where money has went
# an area to input recent transactions
# more to come
'''
def budget_overview(previous_window):
    overview_win = tk.Tk()
    overview_win.title('Budget Overview')
    
    root.destroy()
    previous_window.destroy()

    #Create the labels 

    #Today's date
    today_label = tk.Label(overview_win, text="12, November, 2023")
    today_label.grid(row=0,column=0)





    

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



cursor.close()
cnx.close()