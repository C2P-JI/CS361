import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime
import csv
import os



class UIbudget(tk.Tk):
    def __init__(self, user):
        #create window
        super().__init__() 
        self.title("Monthly Expenses")
        self.user = user
        # self.geometry('800x600')

        self.settings = Settings(self)
        self.settings.grid(row=0, column=0, padx=10, pady=10)

        selected_date = self.settings.get_selected_date()
        self.overview = Overview(self, self.user, selected_date)
        self.overview.grid(row=1, column=0, padx=10)

        self.input = Input(self, user, self.overview)
        self.input.grid(row=2, column=0, padx=10)

        #bind to refresh overview when date changes
        self.settings.select_date.bind("<<DateEntrySelected>>", self.refresh_overview)
        #run 
        self.mainloop()

    def refresh_overview(self,event):
        selected_date = self.settings.get_selected_date()
        self.overview.destroy()
        self.overview = Overview(self,self.user, selected_date)
        self.overview.grid(row=1, column=0, padx=10)

        self.input.destroy()
        self.input = Input(self, self.user, self.overview)
        self.input.grid(row=2, column=0, padx=10)


class Settings(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #display today's date
        today = datetime.date.today()
        self.date_label = ttk.Label(self, text=f"Today's date: {today.strftime('%B %d, %Y')}")
        self.date_label.grid(row=0, column=0, padx=10, pady=10)

        #Select Date
        self.view_date = ttk.Label(self, text="Date Viewing:")
        self.view_date.grid(row=0, column=1, padx=10, pady=10)
        self.select_date = DateEntry(self, width=12, borderwidth=2)
        self.select_date.grid(row=0, column=2, padx=10, pady=10)

    def get_selected_date(self):
        return self.select_date.get_date()

        #dropdown menu for day, week, month, year selection (implement later month view only)
        # timeframe_label = ttk.Label(self, text="Select Timeframe")
        # timeframe_label.grid(row=0, column=3, padx=10, pady=10)
        # self.view = tk.StringVar()
        # self.view_choices = ['Day', 'Week', 'Month', 'Year']
        # self.view_menu = ttk.Combobox(self, textvariable=self.view, values=self.view_choices)
        # self.view_menu.current(2) #default to 'Month'
        # self.view_menu.grid(row=0, column=4, padx=10, pady=10)



        
class Overview(ttk.Frame):
    def __init__(self, parent, user, date):
        super().__init__(parent, relief='groove', padding=(10,10,10,10))
        self.parent = parent
        self.user = user
        self.selected_date = date
        self.info = UserInformation(user)
        self.create_widgets()


    def create_widgets(self):
        self.categories_spending_budget = self.info.get_categories_spending_budget(self.selected_date) #dictionary key is the category name
        next_row = 0
        for idx, (category, data) in enumerate(self.categories_spending_budget.items()):
            budget = int(data['budget'])
            spent = int(data['spent'])
                    
            category_label = ttk.Label(self, text = category, font=("default", 11))
            category_label.grid(row = idx, column = 0, sticky = 'SE', pady= 10)

            barfig = BarFigure(self, category, spent, budget, self.user)
            barfig.grid(row = idx, column = 1, pady = 5)

            budget_label = ttk.Label(self, text = '$' + str(budget))
            budget_label.grid(row = idx, column = 2, sticky = 'S', pady = 5)

            view = ttk.Button(self, text="View All", command=lambda i=idx: self.view_all_transactions(i))
            view.grid(row=idx, column=3, padx=5, pady=5, sticky='S')

            next_row = idx + 1

        category_settings = ttk.Button(self, text="Edit Categories", command=self.cat_settings)
        category_settings.grid(row=next_row, column=0, columnspan=3, sticky="NSEW")

    def refresh_content(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_widgets()

    def cat_settings(self):
        settings_window = tk.Toplevel(self)
        settings_window.title("Edit Categories")

        action_label = ttk.Label(settings_window, text="Available Actions")
       
        add = ttk.Button(settings_window, text="Add New Category", command=self.add_new_category)
        add.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
        
        change = ttk.Button(settings_window, text="Change a Budget", command=self.change_budget)
        change.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")
        
        # rename = ttk.Button(settings_window, text="Rename a Category", command=self.rename_category)
        # rename.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")

        delete = ttk.Button(settings_window, text="Delete a Category", command=self.delete_category)
        delete.grid(row=3, column=0, padx=10, pady=10, sticky="NSEW")
        


    def add_new_category(self):
        #get info name/budget
        window = tk.Toplevel(self)
        category_label = ttk.Label(window, text="Category")
        category_label.grid(row=0, column=0, padx=5)

        budget_label = ttk.Label(window, text="Budget Amount $")
        budget_label.grid(row=1, column=0)

        category_entry = tk.Entry(window)
        category_entry.grid(row=0, column=1, pady=5, padx=10)


        budget_entry = tk.Entry(window) #9digit limit and only numbers allowed
        budget_entry.grid(row=1, column=1, pady=5, padx=10)

        #if entry values do not match self.categories values then update the frame and self.categories
        #need a confirm button to do the function and also the user x outs instead
        return_button = ttk.Button(window, text="Add Category", command=lambda: self.new_category(category_entry.get(), budget_entry.get()))
        return_button.grid(row=2, column=0, columnspan=2)

    def new_category(self, category, budget):
        if self.check_category(category):
           return 
        
        if self.check_budget_value(budget):
            return 
        
        self.categories_spending_budget[category] =({"spent": 0,"budget": budget})

        self.create_new_csv(category, budget)
        self.parent.input.refresh_inputs()
        self.refresh_content()

    def create_new_csv(self, category, budget):
        with open(f"user_db/{self.user}/categories.csv", 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['category', 'budget'])
            writer.writerow({'category': category, 'budget': budget})

        with open(f"user_db/{self.user}/{category}.csv", 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["cost", "description", "date"])
            writer.writeheader

    def check_budget_value(self, budget_value):
        if budget_value.isdigit() and int(budget_value) >= 0:  #can only hold 9 digits 
            if int(budget_value) < 1000000000:
                return False
            else:
                messagebox.showerror("Error", "Budget Amount Exceeds 9 digits")
                return True
        else:
            messagebox.showerror("Error", "Budget Amount must only contain postive integer numbers")
            return True
        
    def check_category(self, new_category):
            if len(new_category) == 0:
                messagebox.showerror("Error", "No name detected in Category")
                return True
            #return true if category already exists
            for category in list(self.categories_spending_budget.keys()):
                if category.lower() == new_category.lower():
                    messagebox.showerror("Error", "That category already exists")
                    return True
            
            return False


    def change_budget(self):
        window = tk.Toplevel(self)
        window.title("Change Budget")

        select_label = ttk.Label(window, text="Select Category")
        select_label.grid(row=0, column=0, padx=10, pady=10)
        category_var = tk.StringVar()
        categories_combobox = ttk.Combobox(window, textvariable=category_var)
        categories_combobox['values'] = list(self.categories_spending_budget.keys())
        categories_combobox.grid(row=0, column=1, padx=10, pady=10)

        new_label = ttk.Label(window, text="New Budget Amount")
        new_label.grid(row=1, column=0, padx=10, pady=10)
        new_budget_entry = ttk.Entry(window)
        new_budget_entry.grid(row=1, column=1, padx=10, pady=10)

        confirm_button = ttk.Button(window, text="Change Budget", 
                                    command=lambda: self.update_budget(category_var.get(), new_budget_entry.get()))
        confirm_button.grid(row=2, column=0, columnspan=2, pady=10)

    def update_budget(self, category, new_budget):
        if self.check_budget_value(new_budget):
            return

        self.categories_spending_budget[category]['budget'] = int(new_budget)
        self.update_categories_csv()
        self.refresh_content()


    def update_categories_csv(self):
        with open(f"user_db/{self.user}/categories.csv", 'w', newline='')as file:
            writer = csv.DictWriter(file, fieldnames=["category", "budget"])
            writer.writeheader()

            for category in list(self.categories_spending_budget.keys()):
                writer.writerow({"category": category, "budget": self.categories_spending_budget[category]["budget"]})



    def delete_category(self):
        window = tk.Toplevel(self)
        window.title("Delete Category")

        ttk.Label(window, text="Select Category").grid(row=0, column=0, padx=10, pady=10)
        category_var = tk.StringVar()
        categories_combobox = ttk.Combobox(window, textvariable=category_var)
        categories_combobox['values'] = list(self.categories_spending_budget.keys())
        categories_combobox.grid(row=0, column=1, padx=10, pady=10)

        delete_button = ttk.Button(window, text="Delete Category", 
                                command=lambda: self.remove_category(category_var.get()))
        delete_button.grid(row=1, column=0, columnspan=2, pady=10)

    def remove_category(self, category):
        if category in self.categories_spending_budget:
            del self.categories_spending_budget[category]
            self.delete_file(category)
            self.update_categories_csv()
            self.parent.input.refresh_inputs()
            self.refresh_content()

    def delete_file(self, category):
        try:
            os.remove(f"user_db/{self.user}/{category}.csv")
            print(f"File {category} has been deleted successfully.")
        except OSError as e:
            print(f"Error: {e}")

    def view_all_transactions(self, idx):
        self.trans_window = tk.Toplevel(self)
        self.category_name = list(self.categories_spending_budget.keys())[idx]
        self.trans_window.title(f"{self.category_name} Transactions")
        self.data = self.read_csv_file(self.category_name)
        
        self.transaction_frames = []
        self.create_trans_frames()


    def create_trans_frames(self):
        for idx, entry in enumerate(self.data):
            frame = ttk.Frame(self.trans_window, relief = 'groove', padding=(10,10,10,10))
            frame.grid(row=idx, sticky="NSEW", padx=5, pady=5)

            cost_label = ttk.Label(frame, text=f"${entry["cost"]}", width=8)
            cost_label.grid(row=0, column=0)

            date_label = ttk.Label(frame, text=f"{entry["date"]}", width=12)
            date_label.grid(row=0, column=1, padx=10)

            description_label = ttk.Label(frame, text=f"{entry["description"]}", width=50)
            description_label.grid(row=0, column=2)

            edit_button = ttk.Button(frame, text="Edit", command=lambda i=idx: self.edit_trans(i))#lamnda i=idx: edit(i)
            edit_button.grid(row=0, column=3)

            delete_button = ttk.Button(frame, text="Delete", command=lambda i2=idx: self.delete_trans(i2))
            delete_button.grid(row=0, column=4)

            self.transaction_frames.append(frame)

        confirm_button = ttk.Button(self.trans_window, text="Confirm Changes", command=self.refresh_content)
        # Get the current last row in the grid
        confirm_button.grid(row = self.grid_size()[1], column=0, columnspan=4)

    def edit_trans(self, idx):
        self.edit_window = tk.Toplevel(self)

        cost_label = ttk.Label(self.edit_window, text = "Cost $")
        cost_label.grid(row=0, column=0)

        self.cost_entry = ttk.Entry(self.edit_window, width = 50)
        self.cost_entry.insert(0, self.data[idx]["cost"])
        self.cost_entry.grid(row=0, column=1)

        description_label = ttk.Label(self.edit_window, text = "Description")
        description_label.grid(row=1, column=0)

        self.description_entry = ttk.Entry(self.edit_window, width = 50)
        self.description_entry.insert(0, self.data[idx]["description"])
        self.description_entry.grid(row=1, column=1)


        date_label = ttk.Label(self.edit_window, text="Date of Entry")
        date_label.grid(row=2, column=0)

        date_str = self.data[idx]["date"]
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        self.date_entry = DateEntry(self.edit_window)
        self.date_entry.set_date(date_obj)
        self.date_entry.grid(row=2, column=1, sticky='W')

        confirm_button = ttk.Button(self.edit_window, text="Confirm Chnages", command=lambda: self.confirm_change(idx))
        confirm_button.grid(row=3, column=0, columnspan=2)

    def confirm_change(self, idx):

        self.data[idx]["cost"] = self.cost_entry.get()
        self.data[idx]["description"] = self.description_entry.get()
        self.data[idx]["date"] = self.date_entry.get_date()
        #write to csv and remake frames
        self.edit_window.destroy()
        self.refresh_trans_frames()

    def refresh_trans_frames(self):
        for widget in self.trans_window.winfo_children():
            widget.destroy()

        self.create_trans_frames()
        self.write_data_to_csv()


    def delete_trans(self, idx):
        del self.data[idx]
        self.refresh_trans_frames()

    def write_data_to_csv(self):
        with open(f"user_db/{self.user}/{self.category_name}.csv", 'w', newline='') as file:
            print("here")
            writer = csv.DictWriter(file, fieldnames=["cost", "description", "date"])
            writer.writeheader()

            for row in self.data:
                writer.writerow(row)

    
    def read_csv_file(self, category):
        data = []
        with open(f"user_db/{self.user}/{category}.csv", 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                entry = {
                    'cost': row['cost'],
                    'description': row['description'],
                    'date': row['date']
                }
                data.append(entry)
        return data



    #add new category
    #change budget
    #change name
    #view information inside of selected category
        


class BarFigure(tk.Canvas):
    def __init__(self, parent, category, spent, budget, user):
        super().__init__(parent, width = 150, height = 39) #initializes canvas width and height
        self.category = category
        self.spent = spent
        self.budget = budget
        self.user = user
        self.draw_bar()

    def draw_bar(self):
        self.create_rectangle(10, 20, 150, 40, outline='black', fill='white')
        filled_length = self.calculate_filled_length()
        fill_color = 'red' if self.spent > self.budget else 'green'
        self.create_rectangle(12, 22, 13 + filled_length, 39, outline='', fill=fill_color)
        # Adjust text placement based on filled length
        text_position = 80 if filled_length > 130 else 10 + filled_length
        self.create_text(text_position, 12, text=f'${self.spent}')

    def calculate_filled_length(self):
        if self.budget == 0:
            return 0
        percent = min(self.spent / self.budget, 1)
        return int(136 * percent)





class Input(ttk.Frame):
    def __init__(self, parent, username, overview):
        super().__init__(parent, relief='groove', padding=(10,10,10,10))
        self.user = username
        self.info = UserInformation(username)
        self.overview = overview
        self.create_input_sections()

    def refresh_inputs(self):
        menu = self.category_option_menu['menu']
        menu.delete(0, 'end')

        new_expense_categories = self.info.get_expense_categories()

        self.category_var.set(new_expense_categories[0])
        for category in new_expense_categories:
            menu.add_command(label=category, command=lambda value=category: self.category_var.set(value))

    def create_input_sections(self):
        expense_categories = self.info.get_expense_categories()
        self.create_section("Expense Input", expense_categories, self.expense_confirmation)
        # self.create_section("Income Input", ["Job"], self.income_confirmation)

    def create_section(self, label, options, confirmation_method):
        row = self.grid_size()[1]  # Get the current last row in the grid
        ttk.Label(self, text=label).grid(row=row, column=0)
        
        self.category_var = tk.StringVar()
        self.category_option_menu = ttk.OptionMenu(self, self.category_var, options[0], *options)
        self.category_option_menu.grid(row=row+1, column=0)
        
        ttk.Label(self, text="$").grid(row=row+1, column=1)
        self.amount_entry = ttk.Entry(self, width=10)
        self.amount_entry.grid(row=row+1, column=2)

        self.description_entry = ttk.Entry(self, width=25)
        self.description_entry.insert(0, "Description")  # Prefill with "Description"
        self.description_entry.grid(row=row+1, column=3)

        self.calendar = DateEntry(self)
        self.calendar.grid(row=row+1, column=4)

        ttk.Button(self, text="Confirm", command=lambda: self.expense_confirmation()).grid(row=row+1, column=5)

    def expense_confirmation(self):
        # Retrieve data from widgets
        category = self.category_var.get()
        amount = self.amount_entry.get()
        description = self.description_entry.get()
        date = self.calendar.get_date()

        # Validate the retrieved data
        if not self.validate_expense_data(amount, description):
            return  # or handle invalid data appropriately

        # Write data to the respective CSV file
        self.write_to_csv(self.user, category, amount, description, date)
        self.overview.refresh_content()

    def validate_expense_data(self, amount, description):
        try:
            # Ensure amount is a valid number
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive")
            # Add more validation checks as needed
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
            return False
        return True

    def write_to_csv(self, user, category, amount, description, date):
        data = {
            "cost": amount,
            "description": description,
            "date": date.strftime('%Y-%m-%d')  # Format date as string
        }

        # Path to the user's category file
        file_path = f"user_db/{user}/{category}.csv"

        # Write data to the CSV file
        with open(file_path, 'a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data.keys())
            if csv_file.tell() == 0:  # Check if the file is empty and write headers
                writer.writeheader()
            writer.writerow(data)



    def validate_numeric_input(self, input_str):
        # Validate that the input is numeric and non-negative
        try:
            value = float(input_str)
            if value < 0:
                raise ValueError("Input should be non-negative.")
            return value
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric value.")
    #         return None


class UserInformation():
    def __init__(self, user):
        self.user = user
        self.path = f"user_db/{user}"
        self.categories = {}

    def get_categories_spending_budget(self, selected_date):
        self.categories_and_budgets()
        self.categories_and_spending(selected_date)
        return self.categories

    def categories_and_budgets(self):
        with open(f"{self.path}/categories.csv", 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.categories[row["category"]] = {"spent": 0, "budget": row["budget"]}

    def categories_and_spending(self, date):
        for category in self.categories:
            with open(f"{self.path}/{category}.csv", 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if self.is_within_date(row['date'], date):
                        self.categories[category]["spent"] += int(row["cost"])

    def is_within_date(self, entry_date, target_date):
        try:
            entry_date_obj = datetime.datetime.strptime(entry_date, '%Y-%m-%d').date()
            return entry_date_obj.month == target_date.month and entry_date_obj.year == target_date.year
        except ValueError as e:
            print(f"Error parsing date {entry_date}: {e}")
            return False  

    def get_expense_categories(self):
        category_list = []
        with open(f"{self.path}/categories.csv", 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category_list.append(row["category"])

        return category_list

