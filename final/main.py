from ui_login import UIlogin
from ui_budget import UIbudget


ui_login = UIlogin()
# user = user_from_text_file()
user = ""
with open("user.txt", 'r+') as file:
    user = file.readline()
    file.truncate(0)
ui_budget = UIbudget(user)