import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os
import csv
from datetime import datetime

class UserRegristration(tk.Toplevel):
    def __init__(self, parent, manager, username):
        super().__init__(parent)
        self.parent = parent
        self.manager=manager
        self.user = username
        self.categories = [{"category": "bills", "budget": "0"},
                            {"category": "entertainment", "budget": "0"},
                            {"category": "food", "budget": "0"},
                            {"category": "shopping", "budget": "0"},
                            {"category": "transportation", "budget": "0"},
                            {"category": "other", "budget": "0"}
                            ]
        self.create_widgets()
        


    def create_widgets(self):
        label1 = ttk.Label(self, text= "Edit Expense Categories", font=("default", 15))
        label1.grid(row=0, column=0, columnspan=3, pady=10)



        self.parent_frame = ttk.Frame(self)
        self.parent_frame.grid(row=1, column=0, columnspan= 3, padx=10,pady=10)

        self.create_frames()


        add_catagory = ttk.Button(self, text="Add Category", command=self.add_catagory)
        add_catagory.grid(row=2, column=0, pady=10)

        confirm_selection = ttk.Button(self, text="Confirm Selection", command=self.confirm)
        confirm_selection.grid(row=2, column=2)


    def edit(self, idx, add=False):
        #get info name/budget
        window = tk.Toplevel(self)
        category_label = ttk.Label(window, text="Category")
        category_label.grid(row=0, column=0, padx=5)

        budget_label = ttk.Label(window, text="Budget Amount $")
        budget_label.grid(row=1, column=0)

        category_entry = tk.Entry(window, )
        if add is False:
            category_entry.insert(0, f"{self.categories[idx]["category"]}")
        category_entry.grid(row=0, column=1, pady=5, padx=10)


        budget_entry = tk.Entry(window) #9digit limit and only numbers allowed
        if add is False:
            budget_entry.insert(0, f"{self.categories[idx]["budget"]}") 
        budget_entry.grid(row=1, column=1, pady=5, padx=10)

        #if entry values do not match self.categories values then update the frame and self.categories
        #need a confirm button to do the function and also the user x outs instead
        if add is False:
            return_button = ttk.Button(window, text="Return", command=lambda: self.edit_category(window, category_entry.get(), budget_entry.get(), idx))
        else:
            return_button = ttk.Button(window, text="Add Category", command=lambda: self.new_category(category_entry.get(), budget_entry.get()))
        return_button.grid(row=2, column=0, columnspan=2)

    def edit_category(self, window, category_name, budget_value, idx):
        if self.check_budget_value(budget_value):
            return
        
        changes = False
        name = False
        value = False
        if category_name != self.categories[idx]["category"]:
            self.categories[idx]["category"] = category_name
            changes = True
            name = True
        
        if budget_value != self.categories[idx]["budget"]:
            self.categories[idx]["budget"] = budget_value
            changes = True
            value = True

        if changes:
            frame = self.frames[idx]
            labels = [widget for widget in frame.winfo_children() if isinstance(widget, ttk.Label)] #gets labels in frame to edit names
            if name:
                labels[0].config(text=self.categories[idx]["category"])
            if value:
                labels[1].config(text=f"${self.categories[idx]["budget"]}")


        print(self.categories[idx])
        window.destroy()


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

    def delete(self, idx):
        #remove from self.categories
        del self.categories[idx]
        self.delete_frames()
        self.create_frames()

    def delete_frames(self):
        for frame in self.frames:
            frame.destroy()

    def add_catagory(self):
        idx = len(self.categories) + 1
        self.edit(idx, add=True)

    def new_category(self, category, budget):
        if self.check_category(category):
           return 
        
        if self.check_budget_value(budget):
            return 
        
        self.categories.append({"category": category, "budget": budget})
        self.delete_frames()
        self.create_frames()

    def check_category(self, new_category):
        if len(new_category) == 0:
            messagebox.showerror("Error", "No name detected in Category")
            return True
        #return true if category already exists
        for category in self.categories:
            if category["category"].lower() == new_category.lower():
                messagebox.showerror("Error", "That category already exists")
                return True
        
        return False


    def create_frames(self):
        self.frames = []
        for idx, category in enumerate(self.categories):
            frame = ttk.Frame(self.parent_frame, relief='groove', padding=(10,10,10,10))
            frame.grid(row=idx)
            
            category_label = ttk.Label(frame, text=category["category"], width=20)
            category_label.grid(row=0, column=0)

            budget_label = ttk.Label(frame, text="$" + category["budget"], width = 10)
            budget_label.grid(row=0, column=1)

            edit_button = ttk.Button(frame, text="Edit", command=lambda i=idx: self.edit(i)) #i captures the index                                                                                                                 
            edit_button.grid(row=0, column=2)                                                #this allows us to edit the frame contents

            delete_button = ttk.Button(frame, text="Delete", command=lambda i2=idx: self.delete(i2))
            delete_button.grid(row=0, column=3)

            self.frames.append(frame)

    def confirm(self):
        #write categories into categories.csv
        #creates csv's for all the user's categories
        path = f"user_db/{self.user}"
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            print("directory already exists")
        
        with open(f"{path}/categories.csv", 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["category", "budget"])
            writer.writeheader()

            for category in self.categories:
                writer.writerow(category)

        for category in self.categories:
            with open(f"{path}/{category["category"]}.csv", 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["cost", "description", "date"])
                writer.writeheader()

        with open("user.txt", 'w') as file:
            file.write(self.user)
        self.parent.destroy()