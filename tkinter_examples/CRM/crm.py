#https://www.youtube.com/watch?v=_RLq1jfapcA&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=28
'''installed the following, all are not necessary but it covers the
    all the bases. 
    download mysql for windows, default settings
    pip install mysql-connector-python-rf
    pip install mysql-connector-python - only this one worked for me
        I had to unistall them all and then reinstall just this one
    pip install mysql-connector
    '''

from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

root = Tk()
root.title('crm example')
root.geometry("400x600")

# Connect to MySQL
mydb = mysql.connector.connect(
        host = "localhost",
        user = "root", 
        password = "^69!d0ingSh!tgood",
        database = "hornybird"
    )

#Check to see if connection to MySQL was created
# print(mydb)

# Create a cursor and initialize it
my_cursor = mydb.cursor()

# Create database (has been ran)
# my_cursor.execute("CREATE DATABASE hornybird")

# Test to see if database was created after running .execute(CREATE DATABASE hornybird)
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)


# Drop table aka delete
#mycursor.execute("DROP TABLE customers")

#USE IF NOT EXISTS avoid comment out
# Create a table (just to be ran one to not create the table every time) (it has been ran)
my_cursor.execute("CREATE TABLE IF NOT EXISTS customers ( \
                    first_name VARCHAR(255), \
                    last_name VARCHAR(255), \
                    zipcode INT(10), \
                    price_paid DECIMAL(10,2), \
                    user_id INT AUTO_INCREMENT PRIMARY KEY)")


#Alter table
'''
my_cursor.execute("ALTER TABLE customers ADD (\
                  email VARCHAR(255), \
                  address_1 VARCHAR(255), \
                  address_2 VARCHAR(255), \
                  city VARCHAR(50), \
                  state VARCHAR(50), \
                  country VARCHAR(255), \
                  phone VARCHAR(255), \
                  payment_method VARCHAR(50), \
                  discount_code VARCHAR(255))")
'''

#show table
# my_cursor.execute("SELECT * FROM customers")
# #print(my_cursor.description)

# for thing in my_cursor.description:
#     print(thing)

#Clear Text Fields
def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address1_box.delete(0, END)
    address2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zipcode_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    #username_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)


#submit customer to database
def add_customer():
    sql_command = "INSERT INTO customers (first_name,\
                                            last_name, \
                                            address_1, \
                                            address_2, \
                                            city, \
                                            state, \
                                            zipcode, \
                                            country, \
                                            phone,\
                                            email, \
                                            payment_method, \
                                            discount_code, \
                                            price_paid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (first_name_box.get(),
              last_name_box.get(),
              address1_box.get(),
              address2_box.get(),
              city_box.get(),
              state_box.get(),
              zipcode_box.get(),
              country_box.get(),
              phone_box.get(),
              email_box.get(),
              payment_method_box.get(),
              discount_code_box.get(),
              price_paid_box.get())
    my_cursor.execute(sql_command, values)
    
    # Commit the changes to the database
    mydb.commit()

    #clear the fields
    clear_fields()


# List Customers
def list_customers():
    list_customer_query = Tk()
    list_customer_query.title("List All Customers")
    list_customer_query.geometry("800x600")

    # Query The Database
    my_cursor.execute("SELECT * FROM customers")
    result = my_cursor.fetchall()
    for index, x in enumerate(result):
        num = 0
        for y in x:    
            lookup_label = Label(list_customer_query, text=y)
            lookup_label.grid(row=index, column=num)
            num +=1


#create a label
title_label = Label(root, text="Customer Database", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

#Create main form to enter customer data
first_name_label = Label(root, text= "First Name")
first_name_label.grid(row=1, column=0, sticky=W, padx=10)

last_name_label = Label(root, text= "Last Name")
last_name_label.grid(row=2, column=0, sticky=W, padx=10)

address1_label = Label(root, text= "Address 1")
address1_label.grid(row=3, column=0, sticky=W, padx=10)

address2_label = Label(root, text= "Address 2")
address2_label.grid(row=4, column=0, sticky=W, padx=10)

city_label = Label(root, text="City")
city_label.grid(row=5, column=0, sticky=W, padx=10)

state_label = Label(root, text= "State")
state_label.grid(row=6, column=0, sticky=W, padx=10)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=7, column=0, sticky=W, padx=10)

country_label = Label(root, text="Country")
country_label.grid(row=8, column=0, sticky=W, padx=10)

phone_label = Label(root, text="Phone Number")
phone_label.grid(row=9, column=0, sticky=W, padx=10)

email_label = Label(root, text="Email Address")
email_label.grid(row=10, column=0, sticky=W, padx=10)

# username_label = Label(root, text="Username")
# username_label.grid(row=11, column=0, sticky=W, padx=10)

payment_method_label = Label(root, text="Payment Method")
payment_method_label.grid(row=11, column=0, sticky=W, padx=10)

discount_code_label = Label(root, text="Discount Code")
discount_code_label.grid(row=12, column=0, sticky=W, padx=10)

price_paid_label = Label(root, text="Price Paid")
price_paid_label.grid(row=13, column=0, sticky=W, padx=10)

#Create Entry Boxes
first_name_box = Entry(root)
first_name_box.grid(row=1, column=1)

last_name_box = Entry(root)
last_name_box.grid(row=2, column=1, pady=5)

address1_box = Entry(root)
address1_box.grid(row=3, column=1, pady=5)

address2_box = Entry(root)
address2_box.grid(row=4, column=1, pady=5)

city_box = Entry(root)
city_box.grid(row=5, column=1, pady=5)

state_box = Entry(root)
state_box.grid(row=6, column=1, pady=5)

zipcode_box = Entry(root)
zipcode_box.grid(row=7, column=1, pady=5)

country_box = Entry(root)
country_box.grid(row=8, column=1, pady=5)

phone_box = Entry(root)
phone_box.grid(row=9, column=1, pady=5)

email_box = Entry(root)
email_box.grid(row=10, column=1, pady=5)

# username_box = Entry(root)
# username_box.grid(row=11, column=1, pady=5)

payment_method_box = Entry(root)
payment_method_box.grid(row=11, column=1, pady=5 )

discount_code_box = Entry(root)
discount_code_box.grid(row=12, column=1, pady=5)

price_paid_box = Entry(root)
price_paid_box.grid(row=13, column=1, pady=5)

# Create Buttons
add_customer_button = Button(root, text="Add Customer To Database", command=add_customer)
add_customer_button.grid(row=14, column=0, padx=10, pady=10)

clear_fields_button = Button(root, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=14, column=1)

#List customer button
list_customers_button = Button(root, text="List Customer", command=list_customers)
list_customers_button.grid(row=15, column=0)


my_cursor.execute("SELECT * FROM customers")
result = my_cursor.fetchall()
for x in result:
    print(x)

root.mainloop()