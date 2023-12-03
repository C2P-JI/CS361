import tkinter as tk
from tkinter import messagebox

from ui_login import UIlogin
from ui_budget import UIbudget


# root = tk.Tk()
# ui = UIlogin(root)
# ui.open_start_window()
# root.mainloop()



#i got the name now we move onto csv file and budget view
# user = ui.get_username()
# print("user: " + user)

user = "yupdude"

# budget_root = tk.Tk()
# ui_budget = UIbudget(budget_root, user)
ui_budget = UIbudget(user)

# budget_root.mainloop()
