import tkinter as tk
from tkinter import messagebox
import rpyc
import ui_login as ui_login_func


# def close_budget_root_app():
#     if messagebox.askokcancel("Quit", "Do you want to quit?"):
#         budget_root.destroy()



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
